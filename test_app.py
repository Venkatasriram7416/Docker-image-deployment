from app import app


def test_home():#we need to create fucntion as test for home route
    response = app.test_client().get("/") #we are making a get request from home page

    assert response.status_code==200 #we are asserting that the status code shoulde be 200
    assert response.data==b"Hello world" #we are asserting that the response data should be "Hello world"
