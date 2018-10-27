**Tests for parsing**

For using tests for any parser you have to run test web server for localhost:

`python tests/test_web_server/flask_test_server.py`

You can check data for any test localhost url in eventer/test/flask_test_server.py

You can check data by browser using address from flask_test_server.py (for example):

`http://127.0.0.1:5000/?source=kudago&testcase=one_event&page=1`

**Tests for answering in messages**

For using tests for answering in messages you have to add environmental variable APIAITOKEN=9f442ba7276d40d1aa64a32a156af507