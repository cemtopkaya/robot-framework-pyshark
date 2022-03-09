*** Settings ***
Documentation     Template robot main suite.

Library    RPA.Browser.Selenium
Library    func.py



*** Tasks ***
Minimal task
    Log    %{PYTHONPATH}
    func.Yaz Dostum
    Log    Cem Done.

# Open a browser and take a screenshot
#     Open Available Browser    http://www.google.com
#     Screenshot
#     Close All Browsers