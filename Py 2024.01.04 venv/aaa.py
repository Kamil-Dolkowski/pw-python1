# import datetime
# import string
# import json



def addf(x):
    return x+1

def test_addf():
    assert addf(1) == 4



class TestParagony:

    def test_addf(self):
        assert addf(1) == 2





# $ pip freeze
# $ pip freeze > requirements.txt
# $ pip install -r requirements.txt     (pobieranie bibliotek, które są zawarte w pliku)

# $ python -m venv test
# $ test/Scripts/activate.bat   ?   (nie korzystalismy ?)
# $ source test/Scripts/activate
# $ deactivate    (deaktywowanie środowiska)
# $ pip uninstall -r requirements.txt   (usuwa biblioteki, które zawarte są w pliku)
# $ pip list
# $ rm -rf test  (usuwanie katalogu z plikami)

# $ python -m pip install django==4.0.0     (pobiera django)
# $ pip freeze > requirements.txt       (dodaje biblioteke django do pliku)
    
# $ pip install pytest
# $ pytest aaa.py
# $ pytest aaa.py -q
        
# $ python -m pytest aaa.py     (to zadziałało)

