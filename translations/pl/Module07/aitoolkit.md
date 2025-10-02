<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T12:42:38+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "pl"
}
-->
# AI Toolkit dla Visual Studio Code - Przewodnik po Edge AI

## Wprowadzenie

Witamy w kompleksowym przewodniku dotyczącym korzystania z AI Toolkit dla Visual Studio Code w rozwoju Edge AI. W miarę jak sztuczna inteligencja przenosi się z centralnego przetwarzania w chmurze na rozproszone urządzenia brzegowe, programiści potrzebują potężnych, zintegrowanych narzędzi, które sprostają unikalnym wyzwaniom wdrożeń brzegowych – od ograniczeń zasobów po wymagania dotyczące pracy offline.

AI Toolkit dla Visual Studio Code wypełnia tę lukę, oferując kompletne środowisko programistyczne zaprojektowane specjalnie do budowy, testowania i optymalizacji aplikacji AI, które działają efektywnie na urządzeniach brzegowych. Niezależnie od tego, czy tworzysz rozwiązania dla czujników IoT, urządzeń mobilnych, systemów wbudowanych czy serwerów brzegowych, ten zestaw narzędzi usprawnia cały proces rozwoju w znanym środowisku VS Code.

Ten przewodnik przeprowadzi Cię przez kluczowe pojęcia, narzędzia i najlepsze praktyki związane z wykorzystaniem AI Toolkit w projektach Edge AI – od wyboru modelu po wdrożenie produkcyjne.

## Przegląd

AI Toolkit dla Visual Studio Code to potężne rozszerzenie, które upraszcza rozwój agentów i tworzenie aplikacji AI. Zestaw narzędzi oferuje kompleksowe możliwości eksploracji, oceny i wdrażania modeli AI od szerokiej gamy dostawców – w tym Anthropic, OpenAI, GitHub, Google – jednocześnie wspierając lokalne wykonywanie modeli za pomocą ONNX i Ollama.

To, co wyróżnia AI Toolkit, to jego kompleksowe podejście do całego cyklu życia rozwoju AI. W przeciwieństwie do tradycyjnych narzędzi, które koncentrują się na pojedynczych aspektach, AI Toolkit zapewnia zintegrowane środowisko obejmujące odkrywanie modeli, eksperymentowanie, rozwój agentów, ocenę i wdrażanie – wszystko w znanym środowisku VS Code.

Platforma została zaprojektowana z myślą o szybkim prototypowaniu i wdrożeniu produkcyjnym, oferując funkcje takie jak generowanie promptów, szybkie starty, bezproblemowe integracje narzędzi MCP (Model Context Protocol) oraz rozbudowane możliwości oceny. W przypadku rozwoju Edge AI oznacza to, że możesz efektywnie tworzyć, testować i optymalizować aplikacje AI dla scenariuszy wdrożeń brzegowych, zachowując pełny przepływ pracy w VS Code.

## Cele nauki

Na koniec tego przewodnika będziesz w stanie:

### Kluczowe kompetencje
- **Zainstalować i skonfigurować** AI Toolkit dla Visual Studio Code w ramach przepływów pracy Edge AI
- **Poruszać się i korzystać** z interfejsu AI Toolkit, w tym Model Catalog, Playground i Agent Builder
- **Wybrać i ocenić** modele AI odpowiednie dla wdrożeń brzegowych, uwzględniając wydajność i ograniczenia zasobów
- **Konwertować i optymalizować** modele za pomocą formatu ONNX i technik kwantyzacji dla urządzeń brzegowych

### Umiejętności rozwoju Edge AI
- **Projektować i wdrażać** aplikacje Edge AI za pomocą zintegrowanego środowiska programistycznego
- **Testować modele** w warunkach przypominających środowisko brzegowe, korzystając z lokalnego wnioskowania i monitorowania zasobów
- **Tworzyć i dostosowywać** agentów AI zoptymalizowanych pod kątem scenariuszy wdrożeń brzegowych
- **Ocenić wydajność modeli** za pomocą metryk istotnych dla obliczeń brzegowych (opóźnienie, użycie pamięci, dokładność)

### Optymalizacja i wdrożenie
- **Stosować techniki kwantyzacji i przycinania** w celu zmniejszenia rozmiaru modelu przy zachowaniu akceptowalnej wydajności
- **Optymalizować modele** dla konkretnych platform sprzętowych brzegowych, w tym CPU, GPU i akceleratorów NPU
- **Wdrażać najlepsze praktyki** w rozwoju Edge AI, w tym zarządzanie zasobami i strategie awaryjne
- **Przygotować modele i aplikacje** do wdrożenia produkcyjnego na urządzeniach brzegowych

### Zaawansowane koncepcje Edge AI
- **Integracja z frameworkami Edge AI** takimi jak ONNX Runtime, Windows ML i TensorFlow Lite
- **Implementacja architektur wielomodelowych** i scenariuszy uczenia federacyjnego dla środowisk brzegowych
- **Rozwiązywanie typowych problemów Edge AI** takich jak ograniczenia pamięci, szybkość wnioskowania i kompatybilność sprzętowa
- **Projektowanie strategii monitorowania i logowania** dla aplikacji Edge AI w produkcji

### Zastosowanie praktyczne
- **Tworzenie kompleksowych rozwiązań Edge AI** od wyboru modelu po wdrożenie
- **Demonstracja biegłości** w przepływach pracy specyficznych dla rozwoju brzegowego i technikach optymalizacji
- **Zastosowanie zdobytej wiedzy** w rzeczywistych przypadkach użycia Edge AI, w tym IoT, aplikacjach mobilnych i wbudowanych
- **Ocena i porównanie** różnych strategii wdrożeń Edge AI oraz ich kompromisów

## Kluczowe funkcje dla rozwoju Edge AI

### 1. Katalog modeli i odkrywanie
- **Wsparcie dla wielu dostawców**: Przeglądaj i uzyskuj dostęp do modeli AI od Anthropic, OpenAI, GitHub, Google i innych dostawców
- **Integracja lokalnych modeli**: Uproszczone odkrywanie modeli ONNX i Ollama dla wdrożeń brzegowych
- **Modele GitHub**: Bezpośrednia integracja z hostingiem modeli GitHub dla uproszczonego dostępu
- **Porównanie modeli**: Porównuj modele obok siebie, aby znaleźć optymalną równowagę dla ograniczeń urządzeń brzegowych

### 2. Interaktywny Playground
- **Interaktywne środowisko testowe**: Szybkie eksperymentowanie z możliwościami modeli w kontrolowanym środowisku
- **Wsparcie multimodalne**: Testowanie z obrazami, tekstem i innymi typowymi wejściami w scenariuszach brzegowych
- **Eksperymentowanie w czasie rzeczywistym**: Natychmiastowa informacja zwrotna na temat odpowiedzi modeli i ich wydajności
- **Optymalizacja parametrów**: Dostosowywanie parametrów modeli do wymagań wdrożeń brzegowych

### 3. Budowanie promptów (Agent Builder)
- **Generowanie języka naturalnego**: Tworzenie początkowych promptów na podstawie opisów w języku naturalnym
- **Iteracyjne udoskonalanie**: Poprawa promptów na podstawie odpowiedzi modeli i ich wydajności
- **Rozkładanie zadań**: Rozbijanie złożonych zadań za pomocą łańcuchów promptów i strukturalnych wyników
- **Wsparcie dla zmiennych**: Używanie zmiennych w promptach dla dynamicznego zachowania agentów
- **Generowanie kodu produkcyjnego**: Tworzenie gotowego do produkcji kodu dla szybkiego rozwoju aplikacji

### 4. Masowe uruchamianie i ocena
- **Testowanie wielu modeli**: Wykonywanie wielu promptów na wybranych modelach jednocześnie
- **Efektywne testowanie na dużą skalę**: Testowanie różnych wejść i konfiguracji w sposób efektywny
- **Niestandardowe przypadki testowe**: Uruchamianie agentów z przypadkami testowymi w celu weryfikacji funkcjonalności
- **Porównanie wydajności**: Porównywanie wyników między różnymi modelami i konfiguracjami

### 5. Ocena modeli za pomocą zbiorów danych
- **Standardowe metryki**: Testowanie modeli AI za pomocą wbudowanych ewaluatorów (F1 score, trafność, podobieństwo, spójność)
- **Niestandardowe ewaluatory**: Tworzenie własnych metryk oceny dla konkretnych przypadków użycia
- **Integracja zbiorów danych**: Testowanie modeli na podstawie kompleksowych zbiorów danych
- **Pomiar wydajności**: Kwantyfikacja wydajności modeli dla decyzji o wdrożeniu brzegowym

### 6. Możliwości dostrajania
- **Dostosowanie modeli**: Dostosowywanie modeli do konkretnych przypadków użycia i dziedzin
- **Specjalistyczna adaptacja**: Adaptacja modeli do specjalistycznych wymagań i dziedzin
- **Optymalizacja brzegowa**: Dostrajanie modeli specjalnie pod kątem ograniczeń wdrożeń brzegowych
- **Trening specyficzny dla dziedziny**: Tworzenie modeli dostosowanych do konkretnych przypadków użycia brzegowego

### 7. Integracja narzędzi MCP
- **Łączność zewnętrzna**: Łączenie agentów z zewnętrznymi narzędziami za pomocą serwerów Model Context Protocol
- **Działania w rzeczywistości**: Umożliwienie agentom zapytań do baz danych, dostępu do API lub wykonywania niestandardowej logiki
- **Istniejące serwery MCP**: Korzystanie z narzędzi z protokołów command (stdio) lub HTTP (server-sent event)
- **Rozwój niestandardowych MCP**: Tworzenie i testowanie nowych serwerów MCP w Agent Builder

### 8. Rozwój i testowanie agentów
- **Wsparcie dla wywoływania funkcji**: Umożliwienie agentom dynamicznego wywoływania zewnętrznych funkcji
- **Testowanie integracji w czasie rzeczywistym**: Testowanie integracji za pomocą uruchomień w czasie rzeczywistym i użycia narzędzi
- **Wersjonowanie agentów**: Kontrola wersji agentów z możliwością porównania wyników oceny
- **Debugowanie i śledzenie**: Lokalna możliwość śledzenia i debugowania dla rozwoju agentów

## Przepływ pracy rozwoju Edge AI

### Faza 1: Odkrywanie i wybór modelu
1. **Eksploracja katalogu modeli**: Korzystaj z katalogu modeli, aby znaleźć modele odpowiednie dla wdrożeń brzegowych
2. **Porównanie wydajności**: Oceń modele na podstawie rozmiaru, dokładności i szybkości wnioskowania
3. **Testowanie lokalne**: Korzystaj z modeli Ollama lub ONNX, aby testować lokalnie przed wdrożeniem brzegowym
4. **Ocena wymagań zasobowych**: Określ potrzeby pamięci i obliczeń dla docelowych urządzeń brzegowych

### Faza 2: Optymalizacja modelu
1. **Konwersja do ONNX**: Konwertuj wybrane modele do formatu ONNX dla kompatybilności brzegowej
2. **Stosowanie kwantyzacji**: Zmniejsz rozmiar modelu za pomocą kwantyzacji INT8 lub INT4
3. **Optymalizacja sprzętowa**: Optymalizuj dla docelowego sprzętu brzegowego (ARM, x86, specjalistyczne akceleratory)
4. **Walidacja wydajności**: Sprawdź, czy zoptymalizowane modele zachowują akceptowalną dokładność

### Faza 3: Rozwój aplikacji
1. **Projektowanie agentów**: Korzystaj z Agent Builder, aby tworzyć zoptymalizowanych agentów AI dla brzegów
2. **Inżynieria promptów**: Twórz prompty, które skutecznie działają z mniejszymi modelami brzegowymi
3. **Testowanie integracji**: Testuj agentów w symulowanych warunkach brzegowych
4. **Generowanie kodu**: Twórz kod produkcyjny zoptymalizowany dla wdrożeń brzegowych

### Faza 4: Ocena i testowanie
1. **Ocena masowa**: Testuj wiele konfiguracji, aby znaleźć optymalne ustawienia brzegowe
2. **Profilowanie wydajności**: Analizuj szybkość wnioskowania, użycie pamięci i dokładność
3. **Symulacja brzegowa**: Testuj w warunkach podobnych do docelowego środowiska wdrożenia brzegowego
4. **Testy obciążeniowe**: Oceń wydajność pod różnymi warunkami obciążenia

### Faza 5: Przygotowanie do wdrożenia
1. **Ostateczna optymalizacja**: Zastosuj końcowe optymalizacje na podstawie wyników testów
2. **Pakowanie wdrożeniowe**: Pakuj modele i kod do wdrożenia brzegowego
3. **Dokumentacja**: Dokumentuj wymagania i konfigurację wdrożenia
4. **Przygotowanie monitorowania**: Przygotuj monitorowanie i logowanie dla wdrożenia brzegowego

## Docelowa grupa odbiorców dla rozwoju Edge AI

### Programiści Edge AI
- Twórcy aplikacji budujących urządzenia brzegowe z AI i rozwiązania IoT
- Programiści systemów wbudowanych integrujący możliwości AI w urządzeniach o ograniczonych zasobach
- Twórcy aplikacji mobilnych tworzący aplikacje AI na urządzeniach mobilnych

### Inżynierowie Edge AI
- Inżynierowie AI optymalizujący modele dla wdrożeń brzegowych i zarządzający pipeline'ami wnioskowania
- Inżynierowie DevOps wdrażający i zarządzający modelami AI w rozproszonej infrastrukturze brzegowej
- Inżynierowie wydajności optymalizujący obciążenia AI dla ograniczeń sprzętowych brzegowych

### Naukowcy i edukatorzy
- Naukowcy AI rozwijający efektywne modele i algorytmy dla obliczeń brzegowych
- Edukatorzy uczący koncepcji Edge AI i demonstrujący techniki optymalizacji
- Studenci uczący się o wyzwaniach i rozwiązaniach w wdrożeniach Edge AI

## Przypadki użycia Edge AI

### Inteligentne urządzenia IoT
- **Rozpoznawanie obrazów w czasie rzeczywistym**: Wdrażanie modeli wizji komputerowej na kamerach IoT i czujnikach
- **Przetwarzanie głosu**: Implementacja rozpoznawania mowy i przetwarzania języka naturalnego na inteligentnych głośnikach
- **Predykcyjne utrzymanie**: Uruchamianie modeli wykrywania anomalii na przemysłowych urządzeniach brzegowych
- **Monitorowanie środowiska**: Wdrażanie modeli analizy danych czujników dla aplikacji środowiskowych

### Aplikacje mobilne i wbudowane
- **Tłumaczenie na urządzeniu**: Implementacja modeli tłumaczenia językowego działających offline
- **Rozszerzona rzeczywistość**: Wdrażanie rozpoznawania obiektów w czasie rzeczywistym i śledzenia dla aplikacji AR
- **Monitorowanie zdrowia**: Uruchamianie modeli analizy zdrowia na urządzeniach noszonych i sprzęcie medycznym
- **Systemy autonomiczne**: Implementacja modeli podejmowania decyzji dla dronów, robotów i pojazdów

### Infrastruktura obliczeń brzegowych
- **Centra danych brzegowych**: Wdrażanie modeli AI w centrach danych brzegowych dla aplikacji o niskim opóźnieniu
- **Integracja CDN**: Integracja możliwości przetwarzania AI w sieciach dostarczania treści
- **Brzeg 5G**: Wykorzystanie obliczeń brzegowych 5G dla aplikacji zasilanych AI
- **Obliczenia mgły**: Implementacja przetwarzania AI w środowiskach obliczeń mgły

## Instalacja i konfiguracja

### Instalacja rozszerzenia
Zainstaluj rozszerzenie AI Toolkit bezpośrednio z Visual Studio Code Marketplace:

**ID rozszerzenia**: `ms-windows-ai-studio.windows-ai-studio`

**Metody instalacji**:
1. **Marketplace VS Code**: Wyszukaj "AI Toolkit" w widoku Extensions
2. **Linia poleceń**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Bezpośrednia instalacja**: Pobierz z [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Wymagania wstępne dla rozwoju Edge AI
- **Visual Studio Code**: Zalecana najnowsza wersja
- **Środowisko Python**: Python 3.8+ z wymaganymi bibliotekami AI
- **ONNX Runtime** (opcjonalnie): Do wnioskowania modeli ONNX
- **Ollama** (opcjonalnie): Do lokalnego serwowania modeli
- **Narzędzia akceleracji sprzętowej**: CUDA, OpenVINO lub akceleratory specyficzne
2. Generowanie początkowych podpowiedzi za pomocą opisów w języku naturalnym  
3. Iteracja i udoskonalanie podpowiedzi na podstawie odpowiedzi modelu  
4. Integracja narzędzi MCP w celu zwiększenia możliwości agenta  

#### Krok 3: Testowanie i ocena  
1. Użyj **Bulk Run**, aby przetestować wiele podpowiedzi na wybranych modelach  
2. Uruchom agentów z przypadkami testowymi, aby zweryfikować funkcjonalność  
3. Oceń dokładność i wydajność za pomocą wbudowanych lub niestandardowych metryk  
4. Porównaj różne modele i konfiguracje  

#### Krok 4: Dostosowanie i optymalizacja  
1. Dostosuj modele do specyficznych przypadków użycia na krawędzi  
2. Zastosuj dostosowanie do specyficznej domeny  
3. Optymalizuj pod kątem ograniczeń wdrożeniowych na krawędzi  
4. Wersjonuj i porównuj różne konfiguracje agentów  

#### Krok 5: Przygotowanie do wdrożenia  
1. Generuj kod gotowy do produkcji za pomocą Agent Builder  
2. Skonfiguruj połączenia serwera MCP do użytku produkcyjnego  
3. Przygotuj pakiety wdrożeniowe dla urządzeń na krawędzi  
4. Skonfiguruj metryki monitorowania i oceny  

## Najlepsze praktyki w rozwoju AI na krawędzi  

### Wybór modelu  
- **Ograniczenia rozmiaru**: Wybierz modele, które mieszczą się w ograniczeniach pamięci docelowych urządzeń  
- **Szybkość wnioskowania**: Priorytetowo traktuj modele z szybkimi czasami wnioskowania dla aplikacji w czasie rzeczywistym  
- **Kompromisy w dokładności**: Równoważ dokładność modelu z ograniczeniami zasobów  
- **Kompatybilność formatu**: Preferuj formaty ONNX lub zoptymalizowane pod kątem sprzętu dla wdrożeń na krawędzi  

### Techniki optymalizacji  
- **Kwantyzacja**: Użyj kwantyzacji INT8 lub INT4, aby zmniejszyć rozmiar modelu i poprawić szybkość  
- **Przycinanie**: Usuń niepotrzebne parametry modelu, aby zmniejszyć wymagania obliczeniowe  
- **Destylacja wiedzy**: Twórz mniejsze modele, które zachowują wydajność większych  
- **Przyspieszenie sprzętowe**: Wykorzystaj NPU, GPU lub specjalistyczne akceleratory, jeśli są dostępne  

### Przebieg pracy rozwojowej  
- **Iteracyjne testowanie**: Testuj często w warunkach podobnych do krawędzi podczas rozwoju  
- **Monitorowanie wydajności**: Ciągle monitoruj użycie zasobów i szybkość wnioskowania  
- **Kontrola wersji**: Śledź wersje modeli i ustawienia optymalizacji  
- **Dokumentacja**: Dokumentuj wszystkie decyzje dotyczące optymalizacji i kompromisy wydajności  

### Rozważania dotyczące wdrożenia  
- **Monitorowanie zasobów**: Monitoruj pamięć, CPU i zużycie energii w produkcji  
- **Strategie awaryjne**: Wdrażaj mechanizmy awaryjne na wypadek awarii modelu  
- **Mechanizmy aktualizacji**: Planuj aktualizacje modeli i zarządzanie wersjami  
- **Bezpieczeństwo**: Wdrażaj odpowiednie środki bezpieczeństwa dla aplikacji AI na krawędzi  

## Integracja z frameworkami AI na krawędzi  

### ONNX Runtime  
- **Wdrożenie międzyplatformowe**: Wdrażaj modele ONNX na różnych platformach krawędziowych  
- **Optymalizacja sprzętu**: Wykorzystaj optymalizacje specyficzne dla sprzętu w ONNX Runtime  
- **Wsparcie mobilne**: Użyj ONNX Runtime Mobile dla aplikacji na smartfony i tablety  
- **Integracja IoT**: Wdrażaj na urządzeniach IoT za pomocą lekkich dystrybucji ONNX Runtime  

### Windows ML  
- **Urządzenia Windows**: Optymalizuj dla urządzeń krawędziowych i komputerów z systemem Windows  
- **Przyspieszenie NPU**: Wykorzystaj Neural Processing Units na urządzeniach Windows  
- **DirectML**: Użyj DirectML do przyspieszenia GPU na platformach Windows  
- **Integracja UWP**: Integruj z aplikacjami Universal Windows Platform  

### TensorFlow Lite  
- **Optymalizacja mobilna**: Wdrażaj modele TensorFlow Lite na urządzeniach mobilnych i wbudowanych  
- **Delegaty sprzętowe**: Użyj specjalistycznych delegatów sprzętowych do przyspieszenia  
- **Mikrokontrolery**: Wdrażaj na mikrokontrolerach za pomocą TensorFlow Lite Micro  
- **Wsparcie międzyplatformowe**: Wdrażaj na Androidzie, iOS i wbudowanych systemach Linux  

### Azure IoT Edge  
- **Hybryda chmura-krawędź**: Łącz trening w chmurze z wnioskowaniem na krawędzi  
- **Wdrożenie modułów**: Wdrażaj modele AI jako moduły IoT Edge  
- **Zarządzanie urządzeniami**: Zdalnie zarządzaj urządzeniami krawędziowymi i aktualizacjami modeli  
- **Telemetria**: Zbieraj dane o wydajności i metryki modeli z wdrożeń na krawędzi  

## Zaawansowane scenariusze AI na krawędzi  

### Wdrożenie wielu modeli  
- **Zespoły modeli**: Wdrażaj wiele modeli dla poprawy dokładności lub redundancji  
- **Testy A/B**: Testuj różne modele jednocześnie na urządzeniach krawędziowych  
- **Dynamiczny wybór**: Wybieraj modele na podstawie aktualnych warunków urządzenia  
- **Współdzielenie zasobów**: Optymalizuj użycie zasobów między wieloma wdrożonymi modelami  

### Federacyjne uczenie  
- **Rozproszone szkolenie**: Szkol modele na wielu urządzeniach krawędziowych  
- **Zachowanie prywatności**: Przechowuj dane szkoleniowe lokalnie, jednocześnie dzieląc się ulepszeniami modeli  
- **Uczenie współpracy**: Umożliwiaj urządzeniom uczenie się na podstawie wspólnych doświadczeń  
- **Koordynacja krawędź-chmura**: Koordynuj uczenie między urządzeniami krawędziowymi a infrastrukturą chmurową  

### Przetwarzanie w czasie rzeczywistym  
- **Przetwarzanie strumieniowe**: Przetwarzaj ciągłe strumienie danych na urządzeniach krawędziowych  
- **Wnioskowanie o niskim opóźnieniu**: Optymalizuj pod kątem minimalnego opóźnienia wnioskowania  
- **Przetwarzanie wsadowe**: Efektywnie przetwarzaj wsady danych na urządzeniach krawędziowych  
- **Przetwarzanie adaptacyjne**: Dostosowuj przetwarzanie na podstawie aktualnych możliwości urządzenia  

## Rozwiązywanie problemów w rozwoju AI na krawędzi  

### Typowe problemy  
- **Ograniczenia pamięci**: Model zbyt duży dla pamięci docelowego urządzenia  
- **Szybkość wnioskowania**: Wnioskowanie modelu zbyt wolne dla wymagań czasu rzeczywistego  
- **Degradacja dokładności**: Optymalizacja obniża dokładność modelu w sposób nieakceptowalny  
- **Kompatybilność sprzętu**: Model niekompatybilny z docelowym sprzętem  

### Strategie debugowania  
- **Profilowanie wydajności**: Użyj funkcji śledzenia AI Toolkit, aby zidentyfikować wąskie gardła  
- **Monitorowanie zasobów**: Monitoruj użycie pamięci i CPU podczas rozwoju  
- **Testowanie inkrementalne**: Testuj optymalizacje stopniowo, aby izolować problemy  
- **Symulacja sprzętu**: Użyj narzędzi rozwojowych do symulacji docelowego sprzętu  

### Rozwiązania optymalizacyjne  
- **Dalsza kwantyzacja**: Zastosuj bardziej agresywne techniki kwantyzacji  
- **Architektura modelu**: Rozważ różne architektury modeli zoptymalizowane dla krawędzi  
- **Optymalizacja przetwarzania wstępnego**: Optymalizuj przetwarzanie danych wstępnych dla ograniczeń krawędziowych  
- **Optymalizacja wnioskowania**: Użyj optymalizacji wnioskowania specyficznych dla sprzętu  

## Zasoby i kolejne kroki  

### Oficjalna dokumentacja  
- [Dokumentacja dla deweloperów AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Przewodnik instalacji i konfiguracji](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Dokumentacja aplikacji inteligentnych VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Dokumentacja Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Społeczność i wsparcie  
- [Repozytorium GitHub AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemy i prośby o funkcje na GitHub](https://aka.ms/AIToolkit/feedback)  
- [Społeczność Discord Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace rozszerzeń VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Zasoby techniczne  
- [Dokumentacja ONNX Runtime](https://onnxruntime.ai/)  
- [Dokumentacja Ollama](https://ollama.ai/)  
- [Dokumentacja Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Dokumentacja Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Ścieżki edukacyjne  
- [Kurs podstaw AI na krawędzi](../Module01/README.md)  
- [Przewodnik po małych modelach językowych](../Module02/README.md)  
- [Strategie wdrożeniowe na krawędzi](../Module03/README.md)  
- [Rozwój AI na krawędzi w Windows](./windowdeveloper.md)  

### Dodatkowe zasoby  
- **Statystyki repozytorium**: Ponad 1,8k gwiazdek, ponad 150 forków, ponad 18 współtwórców  
- **Licencja**: Licencja MIT  
- **Bezpieczeństwo**: Obowiązują zasady bezpieczeństwa Microsoft  
- **Telemetria**: Respektuje ustawienia telemetrii VS Code  

## Podsumowanie  

AI Toolkit dla Visual Studio Code to kompleksowa platforma dla nowoczesnego rozwoju AI, oferująca usprawnione możliwości rozwoju agentów, które są szczególnie wartościowe dla aplikacji AI na krawędzi. Dzięki rozbudowanemu katalogowi modeli wspierającemu dostawców takich jak Anthropic, OpenAI, GitHub i Google, w połączeniu z lokalnym wykonaniem za pomocą ONNX i Ollama, narzędzie oferuje elastyczność potrzebną dla różnorodnych scenariuszy wdrożeniowych na krawędzi.

Siła narzędzia tkwi w jego zintegrowanym podejściu—od odkrywania modeli i eksperymentowania w Playground, przez zaawansowany rozwój agentów z Prompt Builder, kompleksowe możliwości oceny, aż po bezproblemową integrację narzędzi MCP. Dla deweloperów AI na krawędzi oznacza to szybkie prototypowanie i testowanie agentów AI przed wdrożeniem na krawędzi, z możliwością szybkiej iteracji i optymalizacji dla środowisk o ograniczonych zasobach.

Kluczowe zalety dla rozwoju AI na krawędzi obejmują:  
- **Szybkie eksperymentowanie**: Testuj modele i agentów szybko przed wdrożeniem na krawędzi  
- **Elastyczność wielodostawców**: Uzyskaj dostęp do modeli z różnych źródeł, aby znaleźć optymalne rozwiązania na krawędzi  
- **Rozwój lokalny**: Testuj z ONNX i Ollama dla rozwoju offline i ochrony prywatności  
- **Gotowość produkcyjna**: Generuj kod gotowy do produkcji i integruj z zewnętrznymi narzędziami za pomocą MCP  
- **Kompleksowa ocena**: Użyj wbudowanych i niestandardowych metryk do walidacji wydajności AI na krawędzi  

W miarę jak AI coraz bardziej zmierza w kierunku scenariuszy wdrożeniowych na krawędzi, AI Toolkit dla VS Code zapewnia środowisko rozwojowe i przebieg pracy potrzebne do budowy, testowania i optymalizacji inteligentnych aplikacji dla środowisk o ograniczonych zasobach. Niezależnie od tego, czy rozwijasz rozwiązania IoT, aplikacje mobilne AI, czy systemy inteligencji wbudowanej, rozbudowany zestaw funkcji narzędzia i zintegrowany przebieg pracy wspierają cały cykl życia rozwoju AI na krawędzi.

Dzięki ciągłemu rozwojowi i aktywnej społeczności (ponad 1,8k gwiazdek na GitHub), AI Toolkit pozostaje na czele narzędzi rozwojowych AI, stale ewoluując, aby sprostać potrzebom nowoczesnych deweloperów AI budujących dla scenariuszy wdrożeniowych na krawędzi.

[Next Foundry Local](./foundrylocal.md)  

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.