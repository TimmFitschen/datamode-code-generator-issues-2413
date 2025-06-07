from model import Model
from model_workaround import Workaround

test_data = {
 "data": "test",
 "links": {
   "self": "https://localhost:8000/data/test",
   "collection": "https://localhost:8000/data"
 }
}

def test_instanciation():
    model = Model(**test_data)
    print(model.model_dump())
    assert model.links.self is not None
    assert model.links.collection is not None

def test_workaround():
    model = Workaround(**test_data)
    print(model.model_dump())
    assert model.links["self"] is not None
    assert model.links["collection"] is not None
