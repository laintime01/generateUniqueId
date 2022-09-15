import pandas as pd
import uuid

data = pd.DataFrame({
    "id": [uuid.uuid4().hex for _ in range(6)],
    "value": [40,20,10,20,30,50],
    "value2": [1,1,0,0,1,1]
})

data = data.set_index("id")


data2 = pd.DataFrame({
    "id": [uuid.uuid4().hex for _ in range(6)],
    "value": [40,20,10,20,30,50],
    "value2": [1,1,0,0,1,1]
})

data2 = data2.set_index("id")

combined = pd.concat([data, data2], verify_integrity=True)
print(combined)


def test_chances():
    test = uuid.uuid4().hex
    for _ in range(1000000):
        if uuid.uuid4().hex == test:
            print("SAME! uuid sux!")


if __name__ == '__main__':
    test_chances()
