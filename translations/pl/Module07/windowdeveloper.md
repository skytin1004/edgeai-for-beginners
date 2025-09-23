<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9c2dacb560380677a2c923171d3e423d",
  "translation_date": "2025-09-22T13:20:15+00:00",
  "source_file": "Module07/windowdeveloper.md",
  "language_code": "pl"
}
-->
# Przewodnik Rozwoju Windows Edge AI

## Wprowadzenie

Witamy w Windows Edge AI Development - kompleksowym przewodniku po tworzeniu inteligentnych aplikacji wykorzystujących moc AI na urządzeniach dzięki platformie Windows AI Foundry firmy Microsoft. Ten przewodnik jest przeznaczony dla programistów Windows, którzy chcą zintegrować najnowocześniejsze funkcje Edge AI w swoich aplikacjach, korzystając z pełnego zakresu akceleracji sprzętowej Windows.

### Zalety Windows AI

Windows AI Foundry to zintegrowana, niezawodna i bezpieczna platforma wspierająca pełny cykl życia programisty AI - od wyboru modelu i jego dostosowania, po optymalizację i wdrożenie na CPU, GPU, NPU oraz hybrydowych architekturach chmurowych. Platforma ta demokratyzuje rozwój AI, oferując:

- **Abstrakcję sprzętową**: Bezproblemowe wdrożenie na układach AMD, Intel, NVIDIA i Qualcomm
- **Inteligencję na urządzeniu**: AI działające lokalnie, chroniące prywatność użytkownika
- **Optymalizację wydajności**: Modele zoptymalizowane dla konfiguracji sprzętowych Windows
- **Gotowość dla przedsiębiorstw**: Funkcje bezpieczeństwa i zgodności na poziomie produkcyjnym

### Dlaczego Windows dla Edge AI?

**Uniwersalne wsparcie sprzętowe**  
Windows ML automatycznie optymalizuje sprzęt w całym ekosystemie Windows, zapewniając, że aplikacje AI działają optymalnie niezależnie od architektury układu.

**Zintegrowany runtime AI**  
Wbudowany silnik inferencji Windows ML eliminuje skomplikowane wymagania konfiguracji, pozwalając programistom skupić się na logice aplikacji, a nie na problemach infrastrukturalnych.

**Optymalizacja Copilot+ PC**  
Dedykowane API zaprojektowane specjalnie dla urządzeń Windows nowej generacji z wbudowanymi jednostkami przetwarzania neuronowego (NPU), oferujące wyjątkową wydajność na wat.

**Ekosystem dla programistów**  
Bogate narzędzia, w tym integracja z Visual Studio, kompleksowa dokumentacja i przykładowe aplikacje, które przyspieszają cykle rozwoju.

## Cele nauki

Po ukończeniu tego przewodnika rozwoju Windows Edge AI, opanujesz kluczowe umiejętności potrzebne do tworzenia aplikacji AI gotowych do produkcji na platformie Windows.

### Kluczowe kompetencje techniczne

**Opanowanie Windows AI Foundry**  
- Zrozumienie architektury i komponentów platformy Windows AI Foundry  
- Nawigacja po pełnym cyklu rozwoju AI w ekosystemie Windows  
- Wdrażanie najlepszych praktyk bezpieczeństwa dla aplikacji AI na urządzeniach  
- Optymalizacja aplikacji dla różnych konfiguracji sprzętowych Windows  

**Ekspertyza w integracji API**  
- Opanowanie API Windows AI dla aplikacji tekstowych, wizualnych i multimodalnych  
- Wdrażanie integracji modelu językowego Phi Silica dla generowania tekstu i rozumowania  
- Wykorzystanie możliwości widzenia komputerowego za pomocą wbudowanych API przetwarzania obrazów  
- Dostosowywanie modeli wstępnie wytrenowanych za pomocą technik LoRA (Low-Rank Adaptation)  

**Implementacja Foundry Local**  
- Przeglądanie, ocenianie i wdrażanie otwartych modeli językowych za pomocą Foundry Local CLI  
- Zrozumienie optymalizacji modeli i ich kwantyzacji dla lokalnego wdrożenia  
- Wdrażanie funkcji AI offline działających bez połączenia z internetem  
- Zarządzanie cyklem życia modeli i ich aktualizacjami w środowiskach produkcyjnych  

**Wdrożenie Windows ML**  
- Wprowadzanie niestandardowych modeli ONNX do aplikacji Windows za pomocą Windows ML  
- Wykorzystanie automatycznej akceleracji sprzętowej na CPU, GPU i NPU  
- Implementacja inferencji w czasie rzeczywistym z optymalnym wykorzystaniem zasobów  
- Projektowanie skalowalnych aplikacji AI dla różnych kategorii urządzeń Windows  

### Umiejętności tworzenia aplikacji

**Rozwój międzyplatformowy na Windows**  
- Tworzenie aplikacji zasilanych AI za pomocą .NET MAUI dla uniwersalnego wdrożenia na Windows  
- Integracja funkcji AI w aplikacjach Win32, UWP i Progressive Web Applications  
- Implementacja responsywnych projektów UI dostosowujących się do stanów przetwarzania AI  
- Obsługa asynchronicznych operacji AI z odpowiednimi wzorcami doświadczenia użytkownika  

**Optymalizacja wydajności**  
- Profilowanie i optymalizacja wydajności inferencji AI na różnych konfiguracjach sprzętowych  
- Wdrażanie efektywnego zarządzania pamięcią dla dużych modeli językowych  
- Projektowanie aplikacji, które łagodnie degradują się w zależności od dostępnych możliwości sprzętowych  
- Stosowanie strategii buforowania dla często używanych operacji AI  

**Gotowość produkcyjna**  
- Implementacja kompleksowego obsługi błędów i mechanizmów awaryjnych  
- Projektowanie telemetrii i monitorowania wydajności aplikacji AI  
- Stosowanie najlepszych praktyk bezpieczeństwa dla lokalnego przechowywania i wykonywania modeli AI  
- Planowanie strategii wdrożenia dla aplikacji przedsiębiorstw i konsumentów  

### Zrozumienie biznesowe i strategiczne

**Architektura aplikacji AI**  
- Projektowanie hybrydowych architektur optymalizujących przetwarzanie lokalne i chmurowe AI  
- Ocena kompromisów między rozmiarem modelu, dokładnością a szybkością inferencji  
- Planowanie architektur przepływu danych, które zachowują prywatność przy jednoczesnym umożliwieniu inteligencji  
- Wdrażanie opłacalnych rozwiązań AI, które skalują się wraz z wymaganiami użytkowników  

**Pozycjonowanie na rynku**  
- Zrozumienie przewag konkurencyjnych aplikacji AI natywnych dla Windows  
- Identyfikacja przypadków użycia, w których AI na urządzeniu zapewnia lepsze doświadczenia użytkownika  
- Opracowanie strategii wejścia na rynek dla aplikacji Windows wzbogaconych o AI  
- Pozycjonowanie aplikacji w celu wykorzystania korzyści ekosystemu Windows  

## Komponenty platformy Windows AI Foundry

### 1. API Windows AI

API Windows AI oferują gotowe funkcje AI zasilane modelami na urządzeniu, zoptymalizowane pod kątem efektywności i wydajności na urządzeniach Copilot+ PC, wymagając minimalnej konfiguracji.

#### Główne kategorie API

**Model językowy Phi Silica**  
- Mały, ale potężny model językowy do generowania tekstu i rozumowania  
- Zoptymalizowany pod kątem inferencji w czasie rzeczywistym przy minimalnym zużyciu energii  
- Wsparcie dla dostosowywania za pomocą technik LoRA  
- Integracja z wyszukiwaniem semantycznym Windows i odzyskiwaniem wiedzy  

**API widzenia komputerowego**  
- **Rozpoznawanie tekstu (OCR)**: Wyodrębnianie tekstu z obrazów z wysoką dokładnością  
- **Super rozdzielczość obrazu**: Skalowanie obrazów za pomocą lokalnych modeli AI  
- **Segmentacja obrazu**: Identyfikacja i izolowanie konkretnych obiektów na obrazach  
- **Opis obrazu**: Generowanie szczegółowych opisów tekstowych dla treści wizualnych  
- **Usuwanie obiektów**: Usuwanie niechcianych obiektów z obrazów za pomocą AI  

**Funkcje multimodalne**  
- **Integracja wizji i języka**: Łączenie rozumienia tekstu i obrazu  
- **Wyszukiwanie semantyczne**: Umożliwienie zapytań w języku naturalnym w treściach multimedialnych  
- **Odzyskiwanie wiedzy**: Tworzenie inteligentnych doświadczeń wyszukiwania z lokalnymi danymi  

### 2. Foundry Local

Foundry Local zapewnia programistom szybki dostęp do gotowych modeli językowych open-source na Windows Silicon, oferując możliwość przeglądania, testowania, interakcji i wdrażania modeli w lokalnych aplikacjach.

#### Kluczowe funkcje

**Katalog modeli**  
- Kompleksowa kolekcja zoptymalizowanych modeli open-source  
- Modele zoptymalizowane na CPU, GPU i NPU do natychmiastowego wdrożenia  
- Wsparcie dla popularnych rodzin modeli, takich jak Llama, Mistral, Phi i modele specjalistyczne  

**Integracja CLI**  
- Interfejs wiersza poleceń do zarządzania modelami i ich wdrażania  
- Zautomatyzowane przepływy pracy optymalizacji i kwantyzacji  
- Integracja z popularnymi środowiskami programistycznymi i pipeline'ami CI/CD  

**Lokalne wdrożenie**  
- Pełna operacja offline bez zależności od chmury  
- Wsparcie dla niestandardowych formatów i konfiguracji modeli  
- Efektywne serwowanie modeli z automatyczną optymalizacją sprzętową  

### 3. Windows ML

Windows ML jest podstawową platformą AI i zintegrowanym runtime inferencji na Windows, umożliwiając programistom efektywne wdrażanie niestandardowych modeli w szerokim ekosystemie sprzętowym Windows.

#### Korzyści architektury

**Uniwersalne wsparcie sprzętowe**  
- Automatyczna optymalizacja dla układów AMD, Intel, NVIDIA i Qualcomm  
- Wsparcie dla CPU, GPU i NPU z przejrzystym przełączaniem  
- Abstrakcja sprzętowa eliminująca konieczność optymalizacji specyficznej dla platformy  

**Elastyczność modeli**  
- Wsparcie dla formatu modelu ONNX z automatyczną konwersją z popularnych frameworków  
- Wdrożenie niestandardowych modeli z wydajnością na poziomie produkcyjnym  
- Integracja z istniejącymi architekturami aplikacji Windows  

**Integracja dla przedsiębiorstw**  
- Zgodność z ramami bezpieczeństwa i zgodności Windows  
- Wsparcie dla narzędzi wdrożeniowych i zarządzania przedsiębiorstwem  
- Integracja z systemami zarządzania i monitorowania urządzeń Windows  

## Przepływ pracy rozwoju

### Faza 1: Przygotowanie środowiska i konfiguracja narzędzi

**Przygotowanie środowiska programistycznego**  
1. Zainstaluj Visual Studio z rozszerzeniem AI Toolkit  
2. Skonfiguruj narzędzia CLI Windows AI Foundry  
3. Ustaw lokalne środowisko testowania modeli  
4. Skonfiguruj narzędzia do profilowania wydajności i monitorowania  

**Eksploracja AI Dev Gallery**  
- Przeglądaj przykładowe aplikacje i implementacje referencyjne  
- Testuj API Windows AI za pomocą interaktywnych demonstracji  
- Przeglądaj kod źródłowy w poszukiwaniu najlepszych praktyk i wzorców  
- Identyfikuj odpowiednie przykłady dla swojego konkretnego przypadku użycia  

### Faza 2: Wybór i integracja modelu

**Analiza wymagań**  
- Zdefiniuj wymagania funkcjonalne dla funkcji AI  
- Ustal ograniczenia wydajności i cele optymalizacji  
- Oceń wymagania dotyczące prywatności i bezpieczeństwa  
- Zaplanuj architekturę wdrożenia i strategie skalowania  

**Ocena modelu**  
- Użyj Foundry Local do testowania modeli open-source dla swojego przypadku użycia  
- Porównaj API Windows AI z wymaganiami niestandardowych modeli  
- Oceń kompromisy między rozmiarem modelu, dokładnością a szybkością inferencji  
- Prototypuj podejścia integracyjne z wybranymi modelami  

### Faza 3: Tworzenie aplikacji

**Podstawowa integracja**  
- Implementuj integrację API Windows AI z odpowiednią obsługą błędów  
- Projektuj interfejsy użytkownika uwzględniające przepływy pracy przetwarzania AI  
- Wdrażaj strategie buforowania i optymalizacji dla inferencji modeli  
- Dodaj telemetrię i monitorowanie wydajności operacji AI  

**Testowanie i walidacja**  
- Testuj aplikacje na różnych konfiguracjach sprzętowych Windows  
- Waliduj metryki wydajności w różnych warunkach obciążenia  
- Implementuj automatyczne testowanie dla niezawodności funkcji AI  
- Przeprowadzaj testy doświadczenia użytkownika z funkcjami wzbogaconymi o AI  

### Faza 4: Optymalizacja i wdrożenie

**Optymalizacja wydajności**  
- Profiluj wydajność aplikacji na docelowych konfiguracjach sprzętowych  
- Optymalizuj wykorzystanie pamięci i strategie ładowania modeli  
- Implementuj adaptacyjne zachowanie w zależności od dostępnych możliwości sprzętowych  
- Dostosuj doświadczenie użytkownika do różnych scenariuszy wydajności  

**Wdrożenie produkcyjne**  
- Pakuj aplikacje z odpowiednimi zależnościami modeli AI  
- Implementuj mechanizmy aktualizacji dla modeli i logiki aplikacji  
- Konfiguruj monitorowanie i analitykę dla środowisk produkcyjnych  
- Planuj strategie wdrożenia dla przedsiębiorstw i konsumentów  

## Praktyczne przykłady implementacji

### Przykład 1: Inteligentna aplikacja do przetwarzania dokumentów

Stwórz aplikację Windows, która przetwarza dokumenty za pomocą wielu funkcji AI:

**Wykorzystane technologie:**  
- Phi Silica do podsumowywania dokumentów i odpowiadania na pytania  
- API OCR do wyodrębniania tekstu ze skanowanych dokumentów  
- API Opisu Obrazu do analizy wykresów i diagramów  
- Niestandardowe modele ONNX do klasyfikacji dokumentów  

**Podejście do implementacji:**  
- Projektuj modułową architekturę z wtyczkowymi komponentami AI  
- Implementuj asynchroniczne przetwarzanie dla dużych partii dokumentów  
- Dodaj wskaźniki postępu i wsparcie anulowania dla długotrwałych operacji  
- Uwzględnij funkcję offline dla przetwarzania wrażliwych dokumentów  

### Przykład 2: System zarządzania zapasami w handlu detalicznym

Stwórz system zarządzania zapasami zasilany AI dla aplikacji handlowych:

**Wykorzystane technologie:**  
- Segmentacja obrazu do identyfikacji produktów  
- Niestandardowe modele wizji do klasyfikacji marek i kategorii  
- Wdrożenie specjalistycznych modeli językowych handlu detalicznego za pomocą Foundry Local  
- Integracja z istniejącymi systemami POS i zarządzania zapasami  

**Podejście do implementacji:**  
- Buduj integrację z kamerami do skanowania produktów w czasie rzeczywistym  
- Implementuj rozpoznawanie kodów kreskowych i wizualne rozpoznawanie produktów  
- Dodaj naturalne zapytania dotyczące zapasów za pomocą lokalnych modeli językowych  
- Projektuj skalowalną architekturę dla wdrożenia w wielu sklepach  

### Przykład 3: Asystent dokumentacji medycznej

Opracuj narzędzie do dokumentacji medycznej chroniące prywatność:

**Wykorzystane technologie:**  
- Phi Silica do generowania notatek medycznych i wsparcia decyzji klinicznych  
- OCR do digitalizacji ręcznie pisanych dokumentów medycznych  
- Niestandardowe modele językowe medyczne wdrożone za pomocą Windows ML  
- Lokalna pamięć wektorowa do odzyskiwania wiedzy medycznej  

**Podejście do implementacji:**  
- Zapewnij pełną operację offline dla ochrony prywatności pacjenta  
- Implementuj walidację terminologii medycznej i sugestie  
- Dodaj rejestrowanie audytowe dla zgodności regulacyjnej  
- Projektuj integrację z istniejącymi systemami elektronicznej dokumentacji medycznej  

## Strategie optymalizacji wydajności

### Rozwój świadomy sprzętu

**Optymalizacja NPU**  
- Projektuj aplikacje wykorzystujące możliwości NPU na urządzeniach Copilot+ PC  
- Implementuj łagodne przejście na GPU/CPU na urządzeniach bez NPU  
- Optymalizuj formaty modeli dla przyspieszenia specyficznego dla NPU  
- Monitoruj wykorzystanie NPU i charakterystyki termiczne  

**Zarządzanie pamięcią**  
- Implementuj efektywne strategie ładowania i buforowania modeli  
- Używaj mapowania pamięci dla dużych modeli, aby skrócić czas uruchamiania  
- Projektuj aplikacje świadome pamięci dla urządzeń o ograniczonych zasobach  
- Implementuj kwantyzację modeli dla optymalizacji pamięci  

**Efektywność baterii**  
- Optymalizuj operacje AI pod kątem minimalnego zużycia energii  
- Implementuj adaptacyjne przetwarzanie w zależności od stanu baterii  
- Projektuj efektywne przetwarzanie w tle dla ciągłych operacji AI  
- Używaj narzędzi do profilowania energii, aby zoptymalizować zużycie energii  

### Rozważania dotyczące skalowalności

**Wielowątkowość**  
- Projektuj
- Wykorzystaj Foundry Local CLI do testowania i walidacji modeli
- Użyj narzędzi testowych Windows AI API do weryfikacji integracji
- Zaimplementuj niestandardowe logowanie do monitorowania operacji AI
- Stwórz automatyczne testy dla niezawodności funkcjonalności AI

## Przygotowanie aplikacji na przyszłość

### Nowe technologie

**Sprzęt nowej generacji**
- Projektuj aplikacje, aby korzystały z przyszłych możliwości NPU
- Planuj dla większych rozmiarów modeli i ich złożoności
- Wdrażaj adaptacyjne architektury dla rozwijającego się sprzętu
- Rozważ algorytmy gotowe na technologie kwantowe dla przyszłej kompatybilności

**Zaawansowane możliwości AI**
- Przygotuj się na integrację multimodalnej AI z większą liczbą typów danych
- Planuj współpracę AI w czasie rzeczywistym między wieloma urządzeniami
- Projektuj z myślą o możliwościach uczenia federacyjnego
- Rozważ hybrydowe architektury inteligencji edge-cloud

### Ciągłe uczenie się i adaptacja

**Aktualizacje modeli**
- Wdrażaj mechanizmy płynnych aktualizacji modeli
- Projektuj aplikacje, które dostosowują się do ulepszonych możliwości modeli
- Planuj kompatybilność wsteczną z istniejącymi modelami
- Wdrażaj testy A/B do oceny wydajności modeli

**Ewolucja funkcji**
- Projektuj modularne architektury, które uwzględniają nowe możliwości AI
- Planuj integrację nowych Windows AI API
- Wdrażaj flagi funkcji dla stopniowego wprowadzania możliwości
- Projektuj interfejsy użytkownika, które dostosowują się do ulepszonych funkcji AI

## Podsumowanie

Rozwój Windows Edge AI reprezentuje połączenie potężnych możliwości AI z solidną, bezpieczną i skalowalną platformą Windows. Opanowując ekosystem Windows AI Foundry, programiści mogą tworzyć inteligentne aplikacje, które zapewniają wyjątkowe doświadczenia użytkownika, jednocześnie utrzymując najwyższe standardy prywatności, bezpieczeństwa i wydajności.

Połączenie Windows AI API, Foundry Local i Windows ML zapewnia niezrównaną podstawę do budowy kolejnej generacji inteligentnych aplikacji na Windows. W miarę jak AI się rozwija, platforma Windows gwarantuje, że Twoje aplikacje będą skalować się wraz z nowymi technologiami, zachowując kompatybilność i wydajność w różnorodnym ekosystemie sprzętu Windows.

Niezależnie od tego, czy tworzysz aplikacje konsumenckie, rozwiązania dla przedsiębiorstw, czy specjalistyczne narzędzia branżowe, rozwój Windows Edge AI umożliwia tworzenie inteligentnych, responsywnych i głęboko zintegrowanych doświadczeń, które wykorzystują pełny potencjał nowoczesnych urządzeń Windows.

## Dodatkowe zasoby

Aby uzyskać szczegółowy przewodnik po Foundry Local (instalacja, CLI, dynamiczne punkty końcowe, użycie SDK), zobacz przewodnik repozytorium: [foundrylocal.md](./foundrylocal.md).

### Dokumentacja i nauka
- [Windows AI Foundry Documentation](https://learn.microsoft.com/windows/ai/)
- [Windows AI APIs Reference](https://learn.microsoft.com/windows/ai/apis/)
- [Foundry Local Getting Started](https://learn.microsoft.com/windows/ai/foundry-local/get-started/)
- [Windows ML Overview](https://learn.microsoft.com/windows/ai/new-windows-ml/overview/)

### Narzędzia deweloperskie
- [AI Toolkit for Visual Studio Code](https://learn.microsoft.com/windows/ai/toolkit/)
- [AI Dev Gallery](https://learn.microsoft.com/windows/ai/ai-dev-gallery/)
- [Windows AI Samples](https://learn.microsoft.com/windows/ai/samples/)

### Społeczność i wsparcie
- [Windows Developer Community](https://developer.microsoft.com/en-us/windows/)
- [Windows AI Foundry Blog](https://blogs.windows.com/windowsdeveloper/)
- [Microsoft Learn AI Training](https://learn.microsoft.com/training/browse/?products=windows&subjects=artificial-intelligence)

---

*Ten przewodnik został zaprojektowany tak, aby ewoluować wraz z szybko rozwijającym się ekosystemem Windows AI. Regularne aktualizacje zapewniają zgodność z najnowszymi możliwościami platformy i najlepszymi praktykami w zakresie rozwoju.*

---

