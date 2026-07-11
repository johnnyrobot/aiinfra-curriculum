import json, pathlib
# Verified headline figures from AIINFRA_Program_Readiness_Curriculum_Alignment_Report.md §4 (confirmed against EDD source)
VERIFIED = {
 "15-2051":(145554,37.1,40180), "15-1221":(163554,26.1,7690), "15-1252":(179292,18.4,207260),
 "11-3021":(221952,16.5,82270), "15-1241":(163317,11.8,9510), "15-1299":(138203,11.1,59320),
 "15-1211":(131295,9.7,41500), "15-1244":(109420,-4.5,11510)}
d = json.loads(pathlib.Path("site/data/lmi.json").read_text(encoding="utf-8"))
occ = {o["soc"]: o for o in d["occupations"]}
assert set(occ) == set(VERIFIED), "must contain exactly the 8 verified SOCs"
for soc,(med,gr,op) in VERIFIED.items():
    o = occ[soc]
    assert o["medianWage"] == med, f"{soc} median {o['medianWage']}!={med}"
    assert abs(o["growthPct"] - gr) < 0.05, f"{soc} growth {o['growthPct']}!={gr}"
    assert o["openings"] == op, f"{soc} openings {o['openings']}!={op}"
    p = o.get("percentiles") or {}
    if p:  # percentiles are live-sourced; assert ordering when present
        assert p["p10"] <= p["p50"] <= p["p90"], f"{soc} percentile order"
assert d["national"]["value"] > 0 and d["national"]["seriesId"], "national context required"
assert d["meta"]["verifiedAsOf"] and d["meta"]["source"]
print("test_lmi OK")
