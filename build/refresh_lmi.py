import json, os, datetime, urllib.request, urllib.parse, pathlib
OEWS="aef4c53a-7e17-418c-acc1-d189e39b6caa"
CKAN="https://data.ca.gov/api/3/action/datastore_search_sql"
TOP_CODE=239200  # OEWS annual wage top code; censored high percentiles report as ">= this"
VERIFIED=[  # soc, title, base, projected, growthPct, openings, medianWage, meanWage
 ("15-2051","Data Scientists",40400,55400,37.1,40180,145554,159675),
 ("15-1221","Computer & Information Research Scientists",8800,11100,26.1,7690,163554,168344),
 ("15-1252","Software Developers",290800,344400,18.4,207260,179292,190798),
 ("11-3021","Computer & Information Systems Managers",96800,112800,16.5,82270,221952,237025),
 ("15-1241","Computer Network Architects",15300,17100,11.8,9510,163317,154087),
 ("15-1299","Computer Occupations, All Other",84700,94100,11.1,59320,138203,140015),
 ("15-1211","Computer Systems Analysts",62000,68000,9.7,41500,131295,136553),
 ("15-1244","Network & Computer Systems Administrators",26900,25700,-4.5,11510,109420,117612)]
def ckan_sql(sql):
    url=CKAN+"?"+urllib.parse.urlencode({"sql":sql})
    with urllib.request.urlopen(url,timeout=30) as r: return json.load(r)["result"]["records"]
def percentiles(soc):
    # OEWS stores SOC without the hyphen (152051), the statewide all-industries
    # annual figures under Area Name='California', Industry Name='Total, All Industry',
    # Wage Type='Annual wage or salary'.
    try:
        soc6=soc.replace("-","")
        sql=(f'SELECT "Year","Quarter","10th Percentile Wage" p10,"25th Percentile Wage" p25,'
             f'"50th Percentile (Median) Wage" p50,"75th Percentile Wage" p75,"90th Percentile Wage" p90 '
             f'FROM "{OEWS}" WHERE "Area Name"=\'California\' AND "Standard Occupational Classification"=\'{soc6}\' '
             f'AND "Industry Name"=\'Total, All Industry\' AND "Wage Type"=\'Annual wage or salary\' '
             f'AND "50th Percentile (Median) Wage" IS NOT NULL ORDER BY "Year" DESC LIMIT 1')
        r=ckan_sql(sql)
        if not r: return None,None
        row=r[0]
        # OEWS top-codes only the HIGHEST percentiles for top earners (stored null) at the
        # annual top code $239,200 — substitute it there so the band shows "$239,200+".
        # A null low/mid percentile is a different suppression → treat the band as unavailable.
        def f(k, cap_ok):
            v=row[k]
            if v is None or str(v).strip() in ("","None"):
                return TOP_CODE if cap_ok else None
            return int(round(float(str(v).replace(",","").replace("$",""))))
        p10,p25,p50=f("p10",False),f("p25",False),f("p50",False)
        p75,p90=f("p75",True),f("p90",True)
        if None in (p10,p25,p50): return None,None
        return {"p10":p10,"p25":p25,"p50":p50,"p75":p75,"p90":p90}, f'{row["Year"]} {row["Quarter"]}'
    except Exception as e:
        print("percentile fetch failed for",soc,e); return None,None
def bls_national():
    key=os.environ.get("BLS_API_KEY")
    try:
        body={"seriesid":["CES6054150001"],"startyear":"2024","endyear":str(datetime.date.today().year)}
        if key: body["registrationkey"]=key
        req=urllib.request.Request("https://api.bls.gov/publicAPI/v2/timeseries/data/",
            data=json.dumps(body).encode(),headers={"Content-Type":"application/json"})
        with urllib.request.urlopen(req,timeout=30) as r: j=json.load(r)
        pt=j["Results"]["series"][0]["data"][0]
        return {"value":float(pt["value"]),"period":f'{pt["periodName"]} {pt["year"]}'}
    except Exception as e:
        print("BLS fetch failed, using fallback:",e); return {"value":2380.6,"period":"Dec 2025"}
occs=[]; pct_asof=None
for soc,title,base,proj,gr,op,med,mean in VERIFIED:
    pct,asof=percentiles(soc); pct_asof=pct_asof or asof
    occs.append({"soc":soc,"title":title,"base":base,"projected":proj,"growthPct":gr,
                 "openings":op,"medianWage":med,"meanWage":mean,"percentiles":pct})
nat=bls_national()
out={"meta":{"builtAt":datetime.date.today().isoformat(),"projectionsPeriod":"2024-2034",
      "source":"California EDD via data.ca.gov — Long-Term Occupational Projections 2024–2034 + OEWS wages",
      "verifiedAsOf":"May 2024 employment / Q1 2025 wages","percentilesAsOf":pct_asof or "n/a","wageTopCode":TOP_CODE},
     "occupations":occs,
     "national":{"label":"U.S. Computer Systems Design & related services — employment",
                 "seriesId":"CES6054150001","value":nat["value"],"unit":"thousands",
                 "period":nat["period"],"source":"BLS CES"}}
pathlib.Path("site/data/lmi.json").write_text(json.dumps(out,indent=2,ensure_ascii=False),encoding="utf-8")
print("wrote lmi.json — percentilesAsOf",out["meta"]["percentilesAsOf"],"| national",nat)
