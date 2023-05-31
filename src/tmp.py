dict = {"1": {"aa": 1, "a": 3, "aaa": 2, "2131": 3},
        "2": {"b": 2.1, "bb": 2.2}}

q_values = dict["1"]

print(q_values)

print(max(q_values, key=q_values.get))
for i in q_values.values():
        print(i)