# Nomor 1 
def diffDate(x):
    import datetime
    now = datetime.datetime.now()
    from datetime import datetime
    masuk = datetime.strptime(x, "%Y-%m-%d")
    r = masuk - now
    print(abs(r.days))

diffDate("2000-11-12")
