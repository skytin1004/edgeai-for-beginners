<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ab6b3d55f53ea3d498b3c067b17f8816",
  "translation_date": "2025-09-17T16:15:22+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "pl"
}
-->
# AI Toolkit dla Visual Studio Code - Przewodnik po rozwoju Edge AI

## Wprowadzenie

Witamy w kompleksowym przewodniku dotyczącym korzystania z AI Toolkit dla Visual Studio Code w rozwoju Edge AI. W miarę jak sztuczna inteligencja przenosi się z centralnego przetwarzania w chmurze na rozproszone urządzenia brzegowe, programiści potrzebują potężnych, zintegrowanych narzędzi, które sprostają unikalnym wyzwaniom wdrożeń na brzegu - od ograniczeń zasobów po wymagania dotyczące pracy offline.

AI Toolkit dla Visual Studio Code wypełnia tę lukę, oferując kompletne środowisko programistyczne zaprojektowane specjalnie do budowy, testowania i optymalizacji aplikacji AI, które działają efektywnie na urządzeniach brzegowych. Niezależnie od tego, czy tworzysz rozwiązania dla czujników IoT, urządzeń mobilnych, systemów wbudowanych czy serwerów brzegowych, ten zestaw narzędzi upraszcza cały proces rozwoju w znanym środowisku VS Code.

Ten przewodnik przeprowadzi Cię przez kluczowe pojęcia, narzędzia i najlepsze praktyki związane z wykorzystaniem AI Toolkit w projektach Edge AI, od wyboru modelu po wdrożenie produkcyjne.

## Przegląd

AI Toolkit oferuje zintegrowane środowisko programistyczne dla pełnego cyklu życia aplikacji Edge AI w ramach VS Code. Zapewnia płynną integrację z popularnymi modelami AI od dostawców takich jak OpenAI, Anthropic, Google i GitHub, jednocześnie wspierając lokalne wdrożenia modeli za pomocą ONNX i Ollama - kluczowe funkcje dla aplikacji Edge AI wymagających inferencji na urządzeniu.

To, co wyróżnia AI Toolkit w rozwoju Edge AI, to jego skupienie na całym procesie wdrożenia na brzegu. W przeciwieństwie do tradycyjnych narzędzi AI, które głównie koncentrują się na wdrożeniach w chmurze, AI Toolkit zawiera specjalistyczne funkcje do optymalizacji modeli, testowania w warunkach ograniczonych zasobów oraz oceny wydajności specyficznej dla brzegu. Zestaw narzędzi rozumie, że rozwój Edge AI wymaga innych priorytetów - mniejszych rozmiarów modeli, szybszych czasów inferencji, możliwości pracy offline i optymalizacji sprzętowej.

Platforma wspiera różne scenariusze wdrożenia, od prostej inferencji na urządzeniu po złożone architektury wielomodelowe na brzegu. Oferuje narzędzia do konwersji modeli, kwantyzacji i optymalizacji, które są niezbędne do udanego wdrożenia na brzegu, jednocześnie utrzymując produktywność programistów, z której słynie VS Code.

## Cele nauki

Na koniec tego przewodnika będziesz w stanie:

### Podstawowe umiejętności
- **Zainstalować i skonfigurować** AI Toolkit dla Visual Studio Code w ramach przepływów pracy Edge AI
- **Poruszać się i korzystać** z interfejsu AI Toolkit, w tym Model Catalog, Playground i Agent Builder
- **Wybrać i ocenić** modele AI odpowiednie do wdrożenia na brzegu, uwzględniając wydajność i ograniczenia zasobów
- **Konwertować i optymalizować** modele za pomocą formatu ONNX i technik kwantyzacji dla urządzeń brzegowych

### Umiejętności rozwoju Edge AI
- **Projektować i wdrażać** aplikacje Edge AI za pomocą zintegrowanego środowiska programistycznego
- **Testować modele** w warunkach przypominających brzeg, korzystając z lokalnej inferencji i monitorowania zasobów
- **Tworzyć i dostosowywać** agentów AI zoptymalizowanych pod kątem scenariuszy wdrożenia na brzegu
- **Ocenić wydajność modeli** za pomocą metryk istotnych dla obliczeń na brzegu (opóźnienie, zużycie pamięci, dokładność)

### Optymalizacja i wdrożenie
- **Stosować techniki kwantyzacji i przycinania** w celu zmniejszenia rozmiaru modelu przy zachowaniu akceptowalnej wydajności
- **Optymalizować modele** dla specyficznych platform sprzętowych brzegu, w tym CPU, GPU i akceleratorów NPU
- **Wdrażać najlepsze praktyki** w rozwoju Edge AI, w tym zarządzanie zasobami i strategie awaryjne
- **Przygotować modele i aplikacje** do wdrożenia produkcyjnego na urządzeniach brzegowych

### Zaawansowane koncepcje Edge AI
- **Integracja z frameworkami Edge AI** takimi jak ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementacja architektur wielomodelowych** i scenariuszy uczenia federacyjnego dla środowisk brzegu
- **Rozwiązywanie typowych problemów Edge AI** takich jak ograniczenia pamięci, szybkość inferencji i kompatybilność sprzętowa
- **Projektowanie strategii monitorowania i logowania** dla aplikacji Edge AI w produkcji

### Zastosowanie praktyczne
- **Tworzenie kompleksowych rozwiązań Edge AI** od wyboru modelu po wdrożenie
- **Demonstracja biegłości** w przepływach pracy specyficznych dla brzegu i technikach optymalizacji
- **Zastosowanie zdobytej wiedzy** w rzeczywistych przypadkach użycia Edge AI, w tym IoT, aplikacjach mobilnych i wbudowanych
- **Ocena i porównanie** różnych strategii wdrożenia Edge AI oraz ich kompromisów

## Kluczowe funkcje dla rozwoju Edge AI

### 1. Katalog modeli i odkrywanie
- **Wsparcie dla modeli lokalnych**: Odkrywaj i uzyskuj dostęp do modeli AI zoptymalizowanych pod kątem wdrożenia na brzegu
- **Integracja ONNX**: Korzystaj z modeli w formacie ONNX dla efektywnej inferencji na brzegu
- **Wsparcie Ollama**: Wykorzystaj modele działające lokalnie za pomocą Ollama dla prywatności i pracy offline
- **Porównanie modeli**: Porównuj modele obok siebie, aby znaleźć optymalną równowagę między wydajnością a zużyciem zasobów dla urządzeń brzegowych

### 2. Interaktywny Playground
- **Środowisko testowe lokalne**: Testuj modele lokalnie przed wdrożeniem na brzegu
- **Eksperymenty multimodalne**: Testuj obrazy, tekst i inne typowe dane wejściowe w scenariuszach brzegu
- **Dostosowanie parametrów**: Eksperymentuj z różnymi parametrami modeli, aby zoptymalizować je pod kątem ograniczeń brzegu
- **Monitorowanie wydajności w czasie rzeczywistym**: Obserwuj szybkość inferencji i zużycie zasobów podczas rozwoju

### 3. Agent Builder dla aplikacji brzegowych
- **Inżynieria promptów**: Twórz zoptymalizowane prompty, które działają efektywnie z mniejszymi modelami brzegu
- **Integracja narzędzi MCP**: Włącz narzędzia Model Context Protocol dla zwiększonych możliwości agentów brzegu
- **Generowanie kodu**: Twórz kod gotowy do produkcji, zoptymalizowany pod kątem scenariuszy wdrożenia na brzegu
- **Strukturalne wyniki**: Projektuj agentów, którzy dostarczają spójne, strukturalne odpowiedzi odpowiednie dla aplikacji brzegu

### 4. Ocena i testowanie modeli
- **Metryki wydajności**: Oceniaj modele za pomocą metryk istotnych dla wdrożenia na brzegu (opóźnienie, zużycie pamięci, dokładność)
- **Testowanie wsadowe**: Testuj jednocześnie wiele konfiguracji modeli, aby znaleźć optymalne ustawienia brzegu
- **Ocena niestandardowa**: Twórz niestandardowe kryteria oceny specyficzne dla przypadków użycia Edge AI
- **Profilowanie zasobów**: Analizuj wymagania pamięci i obliczeniowe dla planowania wdrożenia na brzegu

### 5. Konwersja i optymalizacja modeli
- **Konwersja ONNX**: Konwertuj modele z różnych formatów na ONNX dla kompatybilności z brzegiem
- **Kwantyzacja**: Zmniejsz rozmiar modelu i popraw szybkość inferencji dzięki technikom kwantyzacji
- **Optymalizacja sprzętowa**: Optymalizuj modele dla specyficznego sprzętu brzegu (CPU, GPU, NPU)
- **Transformacja formatów**: Przekształcaj modele z Hugging Face i innych źródeł dla wdrożenia na brzegu

### 6. Dostosowanie do scenariuszy brzegu
- **Adaptacja domeny**: Dostosuj modele do specyficznych przypadków użycia i środowisk brzegu
- **Trening lokalny**: Trenuj modele lokalnie z obsługą GPU dla specyficznych wymagań brzegu
- **Integracja Azure**: Wykorzystaj Azure Container Apps do treningu w chmurze przed wdrożeniem na brzegu
- **Uczenie transferowe**: Dostosuj modele wstępnie wytrenowane do zadań i ograniczeń specyficznych dla brzegu

### 7. Monitorowanie wydajności i śledzenie
- **Analiza wydajności brzegu**: Monitoruj wydajność modeli w warunkach przypominających brzeg
- **Zbieranie śladów**: Zbieraj szczegółowe dane wydajnościowe dla optymalizacji
- **Identyfikacja wąskich gardeł**: Zidentyfikuj problemy z wydajnością przed wdrożeniem na urządzenia brzegu
- **Śledzenie zużycia zasobów**: Monitoruj pamięć, CPU i czas inferencji dla optymalizacji brzegu

## Przepływ pracy rozwoju Edge AI

### Faza 1: Odkrywanie i wybór modeli
1. **Przeglądaj katalog modeli**: Korzystaj z katalogu modeli, aby znaleźć modele odpowiednie do wdrożenia na brzegu
2. **Porównaj wydajność**: Oceń modele pod kątem rozmiaru, dokładności i szybkości inferencji
3. **Testuj lokalnie**: Korzystaj z modeli Ollama lub ONNX, aby testować lokalnie przed wdrożeniem na brzegu
4. **Oceń wymagania zasobów**: Określ potrzeby pamięci i obliczeniowe dla docelowych urządzeń brzegu

### Faza 2: Optymalizacja modeli
1. **Konwertuj na ONNX**: Konwertuj wybrane modele na format ONNX dla kompatybilności z brzegiem
2. **Stosuj kwantyzację**: Zmniejsz rozmiar modelu za pomocą kwantyzacji INT8 lub INT4
3. **Optymalizacja sprzętowa**: Optymalizuj dla docelowego sprzętu brzegu (ARM, x86, akceleratory specjalistyczne)
4. **Walidacja wydajności**: Sprawdź, czy zoptymalizowane modele zachowują akceptowalną dokładność

### Faza 3: Rozwój aplikacji
1. **Projektowanie agentów**: Korzystaj z Agent Builder, aby tworzyć zoptymalizowanych agentów AI dla brzegu
2. **Inżynieria promptów**: Twórz prompty, które działają efektywnie z mniejszymi modelami
3. **Testowanie integracji**: Testuj agentów w symulowanych warunkach brzegu
4. **Generowanie kodu**: Twórz kod produkcyjny zoptymalizowany pod kątem wdrożenia na brzegu

### Faza 4: Ocena i testowanie
1. **Ocena wsadowa**: Testuj wiele konfiguracji, aby znaleźć optymalne ustawienia brzegu
2. **Profilowanie wydajności**: Analizuj szybkość inferencji, zużycie pamięci i dokładność
3. **Symulacja brzegu**: Testuj w warunkach podobnych do docelowego środowiska wdrożenia na brzegu
4. **Testy obciążeniowe**: Oceń wydajność pod różnymi warunkami obciążenia

### Faza 5: Przygotowanie do wdrożenia
1. **Ostateczna optymalizacja**: Stosuj końcowe optymalizacje na podstawie wyników testów
2. **Pakowanie wdrożeniowe**: Pakuj modele i kod do wdrożenia na brzegu
3. **Dokumentacja**: Dokumentuj wymagania wdrożeniowe i konfigurację
4. **Konfiguracja monitorowania**: Przygotuj monitorowanie i logowanie dla wdrożenia produkcyjnego

## Docelowa grupa odbiorców dla rozwoju Edge AI

### Programiści Edge AI
- Twórcy aplikacji budujących urządzenia brzegowe z AI i rozwiązania IoT
- Programiści systemów wbudowanych integrujący możliwości AI w urządzeniach o ograniczonych zasobach
- Twórcy aplikacji mobilnych tworzący aplikacje AI działające na urządzeniach

### Inżynierowie Edge AI
- Inżynierowie AI optymalizujący modele do wdrożenia na brzegu i zarządzający pipeline'ami inferencji
- Inżynierowie DevOps wdrażający i zarządzający modelami AI w rozproszonej infrastrukturze brzegu
- Inżynierowie wydajności optymalizujący obciążenia AI dla ograniczeń sprzętowych brzegu

### Naukowcy i edukatorzy
- Naukowcy AI rozwijający efektywne modele i algorytmy dla obliczeń na brzegu
- Edukatorzy uczący koncepcji Edge AI i demonstrujący techniki optymalizacji
- Studenci uczący się o wyzwaniach i rozwiązaniach w wdrożeniach Edge AI

## Przypadki użycia Edge AI

### Inteligentne urządzenia IoT
- **Rozpoznawanie obrazów w czasie rzeczywistym**: Wdrażanie modeli wizji komputerowej na kamerach IoT i czujnikach
- **Przetwarzanie głosu**: Implementacja rozpoznawania mowy i przetwarzania języka naturalnego na inteligentnych głośnikach
- **Predykcyjne utrzymanie**: Uruchamianie modeli wykrywania anomalii na przemysłowych urządzeniach brzegu
- **Monitorowanie środowiska**: Wdrażanie modeli analizy danych z czujników dla aplikacji środowiskowych

### Aplikacje mobilne i wbudowane
- **Tłumaczenie na urządzeniu**: Implementacja modeli tłumaczenia językowego działających offline
- **Rozszerzona rzeczywistość**: Wdrażanie rozpoznawania obiektów w czasie rzeczywistym i śledzenia dla aplikacji AR
- **Monitorowanie zdrowia**: Uruchamianie modeli analizy zdrowia na urządzeniach noszonych i sprzęcie medycznym
- **Systemy autonomiczne**: Implementacja modeli podejmowania decyzji dla dronów, robotów i pojazdów

### Infrastruktura obliczeniowa brzegu
- **Centra danych brzegu**: Wdrażanie modeli AI w centrach danych brzegu dla aplikacji o niskim opóźnieniu
- **Integracja CDN**: Integracja możliwości przetwarzania AI w sieciach dostarczania treści
- **Brzeg 5G**: Wykorzystanie obliczeń brzegu 5G dla aplikacji zasilanych AI
- **Obliczenia mgły**: Implementacja przetwarzania AI w środowiskach obliczeń mgły

## Instalacja i konfiguracja

### Szybka instalacja
Zainstaluj rozszerzenie AI Toolkit bezpośrednio z Visual Studio Code Marketplace:

```
Install: AI Toolkit for Visual Studio Code (ms-windows-ai-studio.windows-ai-studio)
```

### Wymagania wstępne dla rozwoju Edge AI
- **ONNX Runtime**: Zainstaluj ONNX Runtime dla inferencji modeli
- **Ollama** (opcjonalnie): Zainstaluj Ollama dla lokalnego serwowania modeli
- **Środowisko Python**: Skonfiguruj Python z wymaganymi bibliotekami AI
- **Narzędzia sprzętowe brzegu**: Zainstaluj narzędzia rozwoju specyficzne dla sprzętu (CUDA, OpenVINO, itp.)

### Konfiguracja początkowa
1. Otwórz VS Code i zainstaluj rozszerzenie AI Toolkit
2. Skonfiguruj źródła modeli (ONNX, Ollama, dostawcy chmurowi)
3. Skonfiguruj lokalne środowisko rozwoju dla testowania brzegu
4. Skonfiguruj opcje akceleracji sprzętowej dla swojej maszyny rozwojowej

## Rozpoczęcie pracy z rozwojem Edge AI

### Krok 1: Wybór modelu
1. Otwórz widok AI Toolkit na pasku aktywności
2. Przeglądaj katalog modeli w poszukiwaniu modeli kompatybilnych z brzegiem
3. Filtruj według rozmiaru modelu, formatu (ONNX) i charakterystyki wydajności
4. Porównaj modele za pomocą wbudowanych narzędzi
- **Bezpieczeństwo**: Wdrożenie odpowiednich środków bezpieczeństwa dla aplikacji AI na urządzeniach brzegowych

## Integracja z frameworkami Edge AI

### ONNX Runtime
- **Wieloplatformowe wdrożenie**: Wdrażanie modeli ONNX na różnych platformach brzegowych
- **Optymalizacja sprzętowa**: Wykorzystanie optymalizacji sprzętowych specyficznych dla ONNX Runtime
- **Wsparcie dla urządzeń mobilnych**: Korzystanie z ONNX Runtime Mobile w aplikacjach na smartfony i tablety
- **Integracja z IoT**: Wdrażanie na urządzeniach IoT za pomocą lekkich dystrybucji ONNX Runtime

### Windows ML
- **Urządzenia z systemem Windows**: Optymalizacja dla urządzeń brzegowych i komputerów z systemem Windows
- **Przyspieszenie NPU**: Wykorzystanie jednostek przetwarzania neuronowego na urządzeniach z Windows
- **DirectML**: Korzystanie z DirectML do przyspieszenia GPU na platformach Windows
- **Integracja z UWP**: Integracja z aplikacjami Universal Windows Platform

### TensorFlow Lite
- **Optymalizacja mobilna**: Wdrażanie modeli TensorFlow Lite na urządzeniach mobilnych i wbudowanych
- **Delegaty sprzętowe**: Wykorzystanie specjalistycznych delegatów sprzętowych do przyspieszenia
- **Mikrokontrolery**: Wdrażanie na mikrokontrolerach za pomocą TensorFlow Lite Micro
- **Wsparcie wieloplatformowe**: Wdrażanie na Androidzie, iOS oraz systemach wbudowanych Linux

### Azure IoT Edge
- **Hybryda chmura-brzeg**: Łączenie trenowania w chmurze z wnioskowaniem na brzegu
- **Wdrażanie modułów**: Wdrażanie modeli AI jako modułów IoT Edge
- **Zarządzanie urządzeniami**: Zdalne zarządzanie urządzeniami brzegowymi i aktualizacjami modeli
- **Telemetria**: Zbieranie danych o wydajności i metrykach modeli z wdrożeń brzegowych

## Zaawansowane scenariusze Edge AI

### Wdrażanie wielu modeli
- **Zespoły modeli**: Wdrażanie wielu modeli dla poprawy dokładności lub redundancji
- **Testy A/B**: Testowanie różnych modeli jednocześnie na urządzeniach brzegowych
- **Dynamiczny wybór**: Wybór modeli w zależności od aktualnych warunków urządzenia
- **Współdzielenie zasobów**: Optymalizacja wykorzystania zasobów między wieloma wdrożonymi modelami

### Federacyjne uczenie
- **Rozproszone trenowanie**: Trenowanie modeli na wielu urządzeniach brzegowych
- **Zachowanie prywatności**: Przechowywanie danych treningowych lokalnie przy jednoczesnym udostępnianiu ulepszeń modeli
- **Uczenie współdzielone**: Umożliwienie urządzeniom uczenia się na podstawie wspólnych doświadczeń
- **Koordynacja brzeg-chmura**: Koordynacja uczenia między urządzeniami brzegowymi a infrastrukturą chmurową

### Przetwarzanie w czasie rzeczywistym
- **Przetwarzanie strumieniowe**: Przetwarzanie ciągłych strumieni danych na urządzeniach brzegowych
- **Wnioskowanie o niskim opóźnieniu**: Optymalizacja pod kątem minimalnego opóźnienia wnioskowania
- **Przetwarzanie wsadowe**: Efektywne przetwarzanie wsadów danych na urządzeniach brzegowych
- **Przetwarzanie adaptacyjne**: Dostosowywanie przetwarzania do aktualnych możliwości urządzenia

## Rozwiązywanie problemów w rozwoju Edge AI

### Typowe problemy
- **Ograniczenia pamięci**: Model zbyt duży dla pamięci docelowego urządzenia
- **Szybkość wnioskowania**: Wnioskowanie modelu zbyt wolne dla wymagań czasu rzeczywistego
- **Spadek dokładności**: Optymalizacja powoduje nieakceptowalny spadek dokładności modelu
- **Kompatybilność sprzętowa**: Model niekompatybilny z docelowym sprzętem

### Strategie debugowania
- **Profilowanie wydajności**: Korzystanie z funkcji śledzenia AI Toolkit w celu identyfikacji wąskich gardeł
- **Monitorowanie zasobów**: Monitorowanie zużycia pamięci i CPU podczas rozwoju
- **Testowanie krok po kroku**: Testowanie optymalizacji krok po kroku w celu izolowania problemów
- **Symulacja sprzętu**: Korzystanie z narzędzi deweloperskich do symulacji docelowego sprzętu

### Rozwiązania optymalizacyjne
- **Dalsza kwantyzacja**: Zastosowanie bardziej agresywnych technik kwantyzacji
- **Architektura modelu**: Rozważenie różnych architektur modeli zoptymalizowanych dla urządzeń brzegowych
- **Optymalizacja wstępnego przetwarzania**: Optymalizacja wstępnego przetwarzania danych pod kątem ograniczeń brzegowych
- **Optymalizacja wnioskowania**: Wykorzystanie optymalizacji wnioskowania specyficznych dla sprzętu

## Zasoby i kolejne kroki

### Dokumentacja
- [AI Toolkit Models Guide](https://code.visualstudio.com/docs/intelligentapps/models)
- [Model Playground Documentation](https://code.visualstudio.com/docs/intelligentapps/playground)
- [ONNX Runtime Documentation](https://onnxruntime.ai/)
- [Windows ML Documentation](https://docs.microsoft.com/en-us/windows/ai/)

### Społeczność i wsparcie
- [VS Code AI Toolkit GitHub](https://github.com/microsoft/vscode-ai-toolkit)
- [ONNX Community](https://github.com/onnx/onnx)
- [Edge AI Developer Community](https://docs.microsoft.com/en-us/azure/iot-edge/community)
- [VS Code Extension Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Zasoby edukacyjne
- [Edge AI Fundamentals Course](./Module01/README.md)
- [Small Language Models Guide](./Module02/README.md)
- [Edge Deployment Strategies](./Module03/README.md)
- [Windows Edge AI Development](./windowdeveloper.md)

## Podsumowanie

AI Toolkit dla Visual Studio Code oferuje kompleksową platformę do rozwoju Edge AI, od odkrywania i optymalizacji modeli po ich wdrożenie i monitorowanie. Dzięki zintegrowanym narzędziom i przepływom pracy, deweloperzy mogą efektywnie tworzyć, testować i wdrażać aplikacje AI, które działają skutecznie na urządzeniach brzegowych o ograniczonych zasobach.

Wsparcie dla ONNX, Ollama oraz różnych dostawców chmurowych, w połączeniu z możliwościami optymalizacji i oceny, czyni AI Toolkit idealnym wyborem dla rozwoju Edge AI. Niezależnie od tego, czy budujesz aplikacje IoT, funkcje AI na urządzenia mobilne, czy systemy inteligencji wbudowanej, AI Toolkit dostarcza narzędzi i przepływów pracy potrzebnych do udanego wdrożenia Edge AI.

W miarę jak Edge AI się rozwija, AI Toolkit dla VS Code pozostaje na czele, oferując deweloperom najnowocześniejsze narzędzia i możliwości do tworzenia kolejnej generacji inteligentnych aplikacji brzegowych.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.