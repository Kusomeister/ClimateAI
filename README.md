ClimateAI
Opis projektu:
Model wykorzystujący warstwy konwolucyjne długiej - krótkiej pamięci (Conv2DLSTM) do analizy szeregów czasowych anomalii temperaturowych w celu przewidzenia kolejnego wyrazu szeregu.

Wejście danych:
Model przyjmuje dane dla 25 (łatwo zmienialne - batch_len) poprzednich miesięcy i przewiduje kolejny. Dane pochodzą z NASA Goddard Institute for Space Studies (Gridded Monthly Temperature Anomaly Data).
Dane są tam dostępne w formacie NetCDF, wykorzystałem [Panoply](https://www.giss.nasa.gov/tools/panoply/) aby przekonwertowac je do formatu CSV.

Zakres danych:
Dane opisują średnie miesięczne anomalie temperaturowe względem średniej dla danego obszaru z lat 1951-1980. Obszary są rozmiaru 2 na 2 stopnie.

Struktura modelu:
Model, poza Conv2DLSTM, wykorzystuje warstwy Conv2D oraz Dropout i regularyzację L1, aby zapobiec przeuczeniu.

Przetwarzanie danych:
Uzupełnianie brakujących danych średnią temperaturą dla danego miesiąca.
Skalowanie danych metodą min-max.
Łączenie miesięcy w serie czasowe.

Prognozy:
W pliku predict.py, uruchamiając model na poprzednich wynikach, prognozujemy ocieplenie do roku 2050 (0,42 stopnia Celsjusza). Rok prognozy można zmienić, ustawiając zmienną rok w predict.py.

Podział danych:
Dane zostały podzielone na treningowe i walidacyjne w sposób losowy za pomocą funkcji train_test_split z sklearn.

Wyniki walidacyjne:

MAE: 0.016
MSE: 0.0086
Dostępność danych:
Ze względu na rozmiar zbioru treningowego, na GitHubie zamieszczone są tylko dane konieczne do uruchomienia predict.py.

Źródła:
GISTEMP Team, 2024: GISS Surface Temperature Analysis (GISTEMP), version 4. NASA Goddard Institute for Space Studies. Dataset accessed 2024-06-12 at [link](https://data.giss.nasa.gov/gistemp/).
Lenssen, N., G. Schmidt, J. Hansen, M. Menne, A. Persin, R. Ruedy, and D. Zyss, 2019: Improvements in the GISTEMP uncertainty model. J. Geophys. Res. Atmos., 124, no. 12, 6307-6326, doi:10.1029/2018JD029522.
