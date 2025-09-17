<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "142e0d1a5b794b8333cfd4895804ced5",
  "translation_date": "2025-09-17T16:06:34+00:00",
  "source_file": "Module07/README.md",
  "language_code": "pl"
}
-->
# Rozdział 07: Przykłady EdgeAI

Edge AI to połączenie sztucznej inteligencji z obliczeniami na urządzeniach brzegowych, umożliwiające inteligentne przetwarzanie bez konieczności korzystania z chmury. Ten rozdział przedstawia pięć różnych implementacji EdgeAI na różnych platformach i w różnych środowiskach, pokazując wszechstronność i możliwości uruchamiania modeli AI na urządzeniach brzegowych.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano to przełom w dostępnych obliczeniach Edge AI, oferujący do 67 TOPS wydajności AI w kompaktowym formacie wielkości karty kredytowej. Ta potężna platforma Edge AI demokratyzuje rozwój generatywnej AI dla hobbystów, studentów i profesjonalnych programistów.

### Kluczowe cechy
- Oferuje do 67 TOPS wydajności AI—1,7 razy więcej niż jego poprzednik
- 1024 rdzenie CUDA i do 32 rdzeni Tensor do przetwarzania AI
- 6-rdzeniowy procesor Arm Cortex-A78AE v8.2 64-bitowy z maksymalną częstotliwością 1,5 GHz
- Cena wynosi zaledwie 249 USD, co czyni platformę najbardziej przystępną dla programistów, studentów i twórców

### Zastosowania
Jetson Orin Nano doskonale radzi sobie z uruchamianiem nowoczesnych modeli generatywnej AI, takich jak transformatory wizji, duże modele językowe i modele wizji-języka. Jest specjalnie zaprojektowany do zastosowań GenAI, a teraz można uruchamiać kilka LLM na urządzeniu wielkości dłoni. Popularne zastosowania obejmują robotykę zasilaną AI, inteligentne drony, inteligentne kamery i autonomiczne urządzenia brzegowe.

**Dowiedz się więcej**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI w aplikacjach mobilnych z .NET MAUI i ONNX Runtime GenAI

To rozwiązanie pokazuje, jak zintegrować generatywną AI i duże modele językowe (LLM) z aplikacjami mobilnymi na różnych platformach, korzystając z .NET MAUI (Multi-platform App UI) i ONNX Runtime GenAI. Podejście to umożliwia programistom .NET tworzenie zaawansowanych aplikacji mobilnych zasilanych AI, które działają natywnie na urządzeniach z Androidem i iOS.

### Kluczowe cechy
- Oparte na frameworku .NET MAUI, zapewniającym jeden kod dla aplikacji na Androida i iOS
- Integracja ONNX Runtime GenAI umożliwia uruchamianie modeli generatywnej AI bezpośrednio na urządzeniach mobilnych
- Obsługuje różne akceleratory sprzętowe dostosowane do urządzeń mobilnych, w tym CPU, GPU i specjalistyczne procesory AI
- Optymalizacje specyficzne dla platform, takie jak CoreML dla iOS i NNAPI dla Androida za pośrednictwem ONNX Runtime
- Implementuje pełny cykl generatywnej AI, w tym przetwarzanie wstępne i końcowe, wnioskowanie, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV

### Korzyści dla programistów
Podejście .NET MAUI pozwala programistom wykorzystać istniejące umiejętności C# i .NET podczas tworzenia aplikacji AI na różnych platformach. Framework ONNX Runtime GenAI obsługuje wiele architektur modeli, w tym Llama, Mistral, Phi, Gemma i wiele innych. Optymalizowane jądra ARM64 przyspieszają mnożenie macierzy INT4, zapewniając wydajność na sprzęcie mobilnym przy zachowaniu znanego środowiska programistycznego .NET.

### Zastosowania
To rozwiązanie jest idealne dla programistów, którzy chcą tworzyć aplikacje mobilne zasilane AI, korzystając z technologii .NET, w tym inteligentne chatboty, aplikacje do rozpoznawania obrazów, narzędzia do tłumaczenia językowego i systemy rekomendacji, które działają całkowicie na urządzeniu, zapewniając większą prywatność i możliwość pracy offline.

**Dowiedz się więcej**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI w Azure z silnikiem Small Language Models

Rozwiązanie EdgeAI oparte na Azure od Microsoftu koncentruje się na efektywnym wdrażaniu Small Language Models (SLM) w środowiskach hybrydowych chmura-brzeg. Podejście to łączy usługi AI na skalę chmury z wymaganiami wdrożeniowymi na brzegu.

### Zalety architektury
- Bezproblemowa integracja z usługami Azure AI
- Uruchamianie SLM/LLM i modeli multimodalnych na urządzeniach i w chmurze za pomocą ONNX Runtime
- Optymalizacja dla wdrożeń na skalę przedsiębiorstwa
- Obsługa ciągłych aktualizacji i zarządzania modelami

### Zastosowania
Implementacja EdgeAI w Azure doskonale sprawdza się w scenariuszach wymagających wdrożeń AI na poziomie przedsiębiorstwa z możliwością zarządzania w chmurze. Obejmuje to inteligentne przetwarzanie dokumentów, analitykę w czasie rzeczywistym i hybrydowe przepływy pracy AI, które wykorzystują zarówno obliczenia w chmurze, jak i na brzegu.

**Dowiedz się więcej**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI z Windows ML

Windows ML to zaawansowany runtime od Microsoftu, zoptymalizowany do wydajnego wnioskowania modeli na urządzeniach i uproszczonego wdrażania, stanowiący podstawę Windows AI Foundry. Platforma ta umożliwia programistom tworzenie aplikacji na Windows zasilanych AI, które wykorzystują pełne możliwości sprzętu PC.

### Możliwości platformy
- Działa na wszystkich komputerach z Windows 11 w wersji 24H2 (build 26100) lub nowszej
- Obsługuje wszystkie komputery x64 i ARM64, nawet te bez NPU czy GPU
- Umożliwia programistom wprowadzenie własnych modeli i ich efektywne wdrażanie w ekosystemie partnerów sprzętowych, w tym AMD, Intel, NVIDIA i Qualcomm, obejmując CPU, GPU, NPU
- Dzięki wykorzystaniu API infrastruktury programiści nie muszą tworzyć wielu wersji aplikacji, aby dostosować je do różnych układów scalonych

### Korzyści dla programistów
Windows ML abstrahuje sprzęt i dostawców wykonania, dzięki czemu możesz skupić się na pisaniu kodu. Ponadto Windows ML automatycznie aktualizuje się, aby obsługiwać najnowsze NPU, GPU i CPU w miarę ich wprowadzania na rynek. Platforma zapewnia jednolity framework do rozwoju AI w różnorodnym ekosystemie sprzętowym Windows.

**Dowiedz się więcej**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](../windowdeveloper.md) - Kompleksowy przewodnik po rozwoju Edge AI na Windows

## 5. EdgeAI z Foundry Local Applications

Foundry Local umożliwia programistom tworzenie aplikacji Retrieval Augmented Generation (RAG) przy użyciu lokalnych zasobów w .NET, łącząc lokalne modele językowe z możliwościami wyszukiwania semantycznego. Podejście to zapewnia rozwiązania AI skoncentrowane na prywatności, które działają całkowicie na lokalnej infrastrukturze.

### Architektura techniczna
- Łączy model językowy Phi-3, lokalne osadzenia i Semantic Kernel, aby stworzyć scenariusz RAG
- Wykorzystuje osadzenia jako wektory (tablice) wartości zmiennoprzecinkowych reprezentujących treść i jej semantyczne znaczenie
- Semantic Kernel działa jako główny orkiestrator, integrując Phi-3 i Smart Components, aby stworzyć płynny pipeline RAG
- Obsługa lokalnych baz danych wektorowych, w tym SQLite i Qdrant

### Korzyści z implementacji
RAG, czyli Retrieval Augmented Generation, to po prostu "wyszukiwanie informacji i włączanie ich do promptu". Ta lokalna implementacja zapewnia prywatność danych, jednocześnie dostarczając inteligentne odpowiedzi oparte na niestandardowych bazach wiedzy. Podejście to jest szczególnie cenne w scenariuszach korporacyjnych wymagających suwerenności danych i możliwości pracy offline.

**Dowiedz się więcej**: [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

## Zasoby do rozwoju EdgeAI na Windows

Dla programistów, którzy koncentrują się na platformie Windows, stworzyliśmy kompleksowy przewodnik obejmujący cały ekosystem Windows EdgeAI. Zasób ten zawiera szczegółowe informacje o Windows AI Foundry, w tym API, narzędzia i najlepsze praktyki w rozwoju EdgeAI na Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry oferuje kompleksowy zestaw narzędzi i API specjalnie zaprojektowanych do rozwoju Edge AI na urządzeniach z Windows. Obejmuje to specjalistyczne wsparcie dla sprzętu przyspieszanego przez NPU, integrację Windows ML i techniki optymalizacji specyficzne dla platformy.

**Kompleksowy przewodnik**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Przewodnik obejmuje:
- Przegląd platformy Windows AI Foundry i jej komponentów
- API Phi Silica do efektywnego wnioskowania na sprzęcie NPU
- API Computer Vision do przetwarzania obrazów i OCR
- Integrację i optymalizację runtime Windows ML
- Foundry Local CLI do lokalnego rozwoju i testowania
- Strategie optymalizacji sprzętu dla urządzeń z Windows
- Praktyczne przykłady implementacji i najlepsze praktyki

### Narzędzia AI do rozwoju Edge AI
Dla programistów korzystających z Visual Studio Code, rozszerzenie AI Toolkit oferuje kompleksowe środowisko rozwoju specjalnie zaprojektowane do tworzenia, testowania i wdrażania aplikacji Edge AI. Narzędzie to upraszcza cały proces rozwoju Edge AI w ramach VS Code.

**Przewodnik rozwoju**: [AI Toolkit for Edge AI Development](../aitoolkit.md)

Przewodnik AI Toolkit obejmuje:
- Odkrywanie i wybór modeli do wdrożeń na brzegu
- Lokalne testowanie i optymalizacja przepływów pracy
- Integrację ONNX i Ollama dla modeli brzegowych
- Techniki konwersji i kwantyzacji modeli
- Rozwój agentów dla scenariuszy brzegowych
- Ocena wydajności i monitorowanie
- Przygotowanie do wdrożenia i najlepsze praktyki

## Podsumowanie

Te pięć implementacji EdgeAI pokazuje dojrzałość i różnorodność dostępnych dziś rozwiązań Edge AI. Od urządzeń brzegowych przyspieszanych sprzętowo, takich jak Jetson Orin Nano, po frameworki programowe, takie jak ONNX Runtime GenAI i Windows ML, programiści mają bezprecedensowe możliwości wdrażania inteligentnych aplikacji na brzegu.

Wspólnym elementem wszystkich tych platform jest demokratyzacja możliwości AI, czyniąc zaawansowane uczenie maszynowe dostępne dla programistów o różnych poziomach umiejętności i w różnych zastosowaniach. Niezależnie od tego, czy tworzysz aplikacje mobilne, oprogramowanie desktopowe czy systemy wbudowane, te rozwiązania EdgeAI stanowią fundament dla nowej generacji inteligentnych aplikacji, które działają wydajnie i prywatnie na brzegu.

Każda platforma oferuje unikalne zalety: Jetson Orin Nano dla obliczeń przyspieszanych sprzętowo, ONNX Runtime GenAI dla rozwoju mobilnego na różnych platformach, Azure EdgeAI dla integracji chmura-brzeg na poziomie przedsiębiorstwa, Windows ML dla natywnych aplikacji na Windows oraz Foundry Local dla implementacji RAG skoncentrowanych na prywatności. Razem tworzą kompleksowy ekosystem dla rozwoju EdgeAI.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.