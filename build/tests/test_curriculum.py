import json, pathlib
VERIFIED_SOCS = {"15-2051","15-1221","15-1252","11-3021","15-1241","15-1299","15-1211","15-1244"}
ORDER = ["100","101","102","200","201","202","300","301","302","303"]
NEXT = dict(zip(ORDER, ORDER[1:]+[None]))
d = json.loads(pathlib.Path("site/data/curriculum.json").read_text(encoding="utf-8"))
p = d["program"]; s = p["stats"]
assert s == {"courses":10,"contactHours":540,"unitEquivalent":30,"semesters":3,"weeksPerCourse":16,"hoursPerCourse":54}, s
assert [c["code"] for c in d["courses"]] == ORDER, "courses must be in canonical order"
sem_courses = {c for sem in p["semesters"] for c in sem["courses"]}
assert sem_courses == set(ORDER) and sum(len(x["courses"]) for x in p["semesters"]) == 10
for c in d["courses"]:
    for f in ("title","subtitle","description","objectives","slos","weeks","tools","socs","prereq"):
        assert c.get(f), f"{c['code']} missing {f}"
    assert len(c["objectives"]) >= 4 and len(c["slos"]) >= 4, c["code"]
    assert [w["n"] for w in c["weeks"]] == list(range(1,17)), f"{c['code']} needs weeks 1..16"
    for w in c["weeks"]:
        assert w["title"] and w["summary"], f"{c['code']} wk{w['n']} empty"
    assert c["midtermWeek"] == 8 and c["capstoneWeek"] == 16
    assert set(c["socs"]) <= VERIFIED_SOCS, f"{c['code']} bad SOC {c['socs']}"
    assert c["next"] == NEXT[c["code"]], f"{c['code']} next chain wrong"
    assert c["hours"] == 54
print("test_curriculum OK —", len(d["courses"]), "courses")
