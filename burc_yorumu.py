import requests
from bs4 import BeautifulSoup

def BurcYorumu (burc):
  burcArr = ["koc", "boga", "ikizler", "yengec", "aslan", "basak", "terazi", "oglak", "akrep", "yay", "kova", "balik" ]
  if(burc in burcArr):
    url = "https://www.hurriyet.com.tr/mahmure/astroloji/"+burc+"-burcu/"

    # Sayfayı indir
    response = requests.get(url)
    html = response.text

    # BeautifulSoup ile sayfa içeriğini analiz et
    soup = BeautifulSoup(html, 'html.parser')

    # Belirli bir div'i ve içeriğini bul
    div_class = "horoscope-detail-tab-content"  # Hedef div'in sınıf adı
    target_div = soup.find("div", class_=div_class)

    if target_div:
        # Hedef div içindeki tüm <p> etiketlerini al
        p_tags = target_div.find_all("p")

        # İkinci <p> etiketini seç
        if len(p_tags) > 1:
            second_p_tag = p_tags[1].text
            return(second_p_tag)
    else:
        return "Falcı kriz geçirdi sonra tekrar deneyelim mi balım?"
  else:
    return("koc, boga, ikizler, yengec, aslan, basak, terazi, oglak, akrep, yay, kova, balik değerlerinden biri ile tekrar dener misin?")

