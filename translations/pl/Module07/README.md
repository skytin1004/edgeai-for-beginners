<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e9e31a2b5ff0f6a682a258fa859a8ff5",
  "translation_date": "2025-09-26T19:33:39+00:00",
  "source_file": "Module07/README.md",
  "language_code": "pl"
}
-->
# Rozdział 07: Przykłady EdgeAI

Edge AI to połączenie sztucznej inteligencji z obliczeniami na urządzeniach brzegowych, umożliwiające inteligentne przetwarzanie danych bez konieczności korzystania z chmury. Ten rozdział przedstawia pięć różnych implementacji EdgeAI na różnych platformach i w różnych środowiskach, ukazując wszechstronność i możliwości uruchamiania modeli AI na urządzeniach brzegowych.

## 1. EdgeAI na NVIDIA Jetson Orin Nano

NVIDIA Jetson Orin Nano to przełom w dostępnych rozwiązaniach Edge AI, oferujący do 67 TOPS wydajności AI w kompaktowym formacie wielkości karty kredytowej. Ta potężna platforma Edge AI demokratyzuje rozwój generatywnej AI dla hobbystów, studentów i profesjonalnych programistów.

### Kluczowe cechy
- Oferuje do 67 TOPS wydajności AI — 1,7 razy więcej niż jego poprzednik
- 1024 rdzenie CUDA i do 32 rdzeni Tensor do przetwarzania AI
- 6-rdzeniowy procesor Arm Cortex-A78AE v8.2 64-bit o maksymalnej częstotliwości 1,5 GHz
- Cena wynosi zaledwie 249 USD, co czyni platformę najbardziej przystępną dla programistów, studentów i twórców

### Zastosowania
Jetson Orin Nano doskonale radzi sobie z uruchamianiem nowoczesnych modeli generatywnej AI, takich jak transformatory wizji, duże modele językowe i modele wizji-języka. Jest specjalnie zaprojektowany do zastosowań GenAI, umożliwiając uruchamianie wielu LLM na urządzeniu wielkości dłoni. Popularne zastosowania obejmują robotykę zasilaną AI, inteligentne drony, inteligentne kamery i autonomiczne urządzenia brzegowe.

**Dowiedz się więcej**: [NVIDIA's Jetson Orin Nano SuperComputer: The Next Big Thing in EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI w aplikacjach mobilnych z .NET MAUI i ONNX Runtime GenAI

To rozwiązanie pokazuje, jak zintegrować generatywną AI i duże modele językowe (LLM) z aplikacjami mobilnymi na różnych platformach, korzystając z .NET MAUI (Multi-platform App UI) i ONNX Runtime GenAI. Podejście to umożliwia programistom .NET tworzenie zaawansowanych aplikacji mobilnych zasilanych AI, które działają natywnie na urządzeniach z Androidem i iOS.

### Kluczowe cechy
- Oparte na frameworku .NET MAUI, zapewniającym jeden kod dla aplikacji na Androida i iOS
- Integracja ONNX Runtime GenAI umożliwia uruchamianie modeli generatywnej AI bezpośrednio na urządzeniach mobilnych
- Obsługuje różne akceleratory sprzętowe dostosowane do urządzeń mobilnych, w tym CPU, GPU i specjalistyczne procesory AI
- Optymalizacje specyficzne dla platform, takie jak CoreML dla iOS i NNAPI dla Androida, dzięki ONNX Runtime
- Implementuje pełny cykl generatywnej AI, w tym przetwarzanie wstępne i końcowe, wnioskowanie, przetwarzanie logitów, wyszukiwanie i próbkowanie oraz zarządzanie pamięcią podręczną KV

### Korzyści dla programistów
Podejście .NET MAUI pozwala programistom wykorzystać istniejące umiejętności w C# i .NET, tworząc aplikacje AI na różnych platformach. Framework ONNX Runtime GenAI obsługuje wiele architektur modeli, takich jak Llama, Mistral, Phi, Gemma i inne. Optymalizowane jądra ARM64 przyspieszają mnożenie macierzy INT4, zapewniając wydajność na sprzęcie mobilnym przy zachowaniu znanego środowiska programistycznego .NET.

### Zastosowania
Rozwiązanie to jest idealne dla programistów, którzy chcą tworzyć aplikacje mobilne zasilane AI, korzystając z technologii .NET, w tym inteligentne chatboty, aplikacje do rozpoznawania obrazów, narzędzia do tłumaczenia językowego i systemy rekomendacji działające całkowicie na urządzeniu, zapewniając większą prywatność i możliwość pracy offline.

**Dowiedz się więcej**: [.NET MAUI ONNX Runtime GenAI Example](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI w Azure z silnikiem Small Language Models

Rozwiązanie EdgeAI oparte na Azure od Microsoftu koncentruje się na efektywnym wdrażaniu małych modeli językowych (SLM) w środowiskach hybrydowych chmura-brzeg. Podejście to łączy skalowalne usługi AI w chmurze z wymaganiami wdrożeń na urządzeniach brzegowych.

### Zalety architektury
- Bezproblemowa integracja z usługami Azure AI
- Uruchamianie SLM/LLM i modeli multimodalnych na urządzeniach oraz w chmurze dzięki ONNX Runtime
- Optymalizacja dla wdrożeń na skalę przedsiębiorstwa
- Obsługa ciągłych aktualizacji i zarządzania modelami

### Zastosowania
Implementacja EdgeAI w Azure sprawdza się w scenariuszach wymagających wdrożeń AI na poziomie przedsiębiorstwa z możliwością zarządzania w chmurze. Obejmuje to inteligentne przetwarzanie dokumentów, analitykę w czasie rzeczywistym i hybrydowe przepływy pracy AI, które wykorzystują zarówno zasoby chmury, jak i urządzeń brzegowych.

**Dowiedz się więcej**: [Azure EdgeAI SLM Engine](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## [4. EdgeAI z Windows ML](./windowdeveloper.md)

Windows ML to zaawansowany runtime Microsoftu zoptymalizowany do wydajnego wnioskowania modeli na urządzeniach oraz uproszczonego wdrażania, stanowiący podstawę Windows AI Foundry. Platforma ta umożliwia programistom tworzenie aplikacji AI na Windows, które wykorzystują pełne możliwości sprzętu PC.

### Możliwości platformy
- Działa na wszystkich komputerach z Windows 11 w wersji 24H2 (build 26100) lub nowszej
- Obsługuje wszystkie komputery x64 i ARM64, nawet te bez NPU czy GPU
- Umożliwia programistom wdrażanie własnych modeli efektywnie na ekosystemie partnerów sprzętowych, w tym AMD, Intel, NVIDIA i Qualcomm, obejmując CPU, GPU, NPU
- Dzięki API infrastruktury programiści nie muszą tworzyć wielu wersji aplikacji, aby dostosować je do różnych układów scalonych

### Korzyści dla programistów
Windows ML abstrahuje sprzęt i dostawców wykonania, dzięki czemu możesz skupić się na pisaniu kodu. Ponadto Windows ML automatycznie aktualizuje się, aby obsługiwać najnowsze NPU, GPU i CPU w miarę ich wydawania. Platforma zapewnia jednolity framework do rozwoju AI na różnorodnym sprzęcie Windows.

**Dowiedz się więcej**: 
- [Windows ML Overview](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Windows EdgeAI Development Guide](./windowdeveloper.md) - Kompleksowy przewodnik po rozwoju Edge AI na Windows

## [5. EdgeAI z Foundry Local Applications](./foundrylocal.md)

Foundry Local umożliwia programistom Windows i Mac tworzenie aplikacji Retrieval Augmented Generation (RAG) przy użyciu lokalnych zasobów w .NET, łącząc lokalne modele językowe z możliwościami wyszukiwania semantycznego. Podejście to zapewnia rozwiązania AI skoncentrowane na prywatności, które działają całkowicie na lokalnej infrastrukturze.

### Architektura techniczna
- Łączy model językowy Phi, lokalne osadzenia i Semantic Kernel, tworząc scenariusz RAG
- Wykorzystuje osadzenia jako wektory (tablice) wartości zmiennoprzecinkowych reprezentujących treść i jej semantyczne znaczenie
- Semantic Kernel działa jako główny koordynator, integrując Phi i Smart Components, aby stworzyć płynny pipeline RAG
- Obsługa lokalnych baz danych wektorowych, takich jak SQLite i Qdrant

### Korzyści z implementacji
RAG, czyli Retrieval Augmented Generation, to po prostu "wyszukiwanie informacji i włączanie ich do promptu". Lokalna implementacja zapewnia prywatność danych, jednocześnie dostarczając inteligentne odpowiedzi oparte na niestandardowych bazach wiedzy. Podejście to jest szczególnie cenne w scenariuszach przedsiębiorstw wymagających suwerenności danych i możliwości pracy offline.

**Dowiedz się więcej**: 
- [Foundry Local](./foundrylocal.md)
- [Foundry Local RAG Samples](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Windows Foundry Local

Microsoft Foundry Local oferuje serwer REST kompatybilny z OpenAI, zasilany przez ONNX Runtime, umożliwiający uruchamianie modeli lokalnie na Windows. Poniżej znajduje się szybkie podsumowanie; pełne szczegóły znajdziesz w oficjalnej dokumentacji.

- Rozpocznij: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Architektura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referencja CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Pełny przewodnik dla Windows w tym repozytorium: [foundrylocal.md](./foundrylocal.md)

Instalacja lub aktualizacja na Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Eksploracja kategorii CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Uruchom model i odkryj dynamiczny punkt końcowy:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Szybka kontrola REST, aby wyświetlić listę modeli (zamień PORT ze statusu):
```cmd
curl -s http://localhost:PORT/v1/models
```

Wskazówki:
- Integracja SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Własny model (kompilacja): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Zasoby dla rozwoju EdgeAI na Windows

Dla programistów celujących w platformę Windows stworzyliśmy kompleksowy przewodnik, który obejmuje cały ekosystem Windows EdgeAI. Zasób ten dostarcza szczegółowych informacji o Windows AI Foundry, w tym API, narzędziach i najlepszych praktykach dla rozwoju EdgeAI na Windows.

### Platforma Windows AI Foundry
Platforma Windows AI Foundry oferuje kompleksowy zestaw narzędzi i API specjalnie zaprojektowanych do rozwoju Edge AI na urządzeniach z Windows. Obejmuje to specjalistyczne wsparcie dla sprzętu przyspieszanego przez NPU, integrację Windows ML i techniki optymalizacji specyficzne dla platformy.

**Kompleksowy przewodnik**: [Windows EdgeAI Development Guide](../windowdeveloper.md)

Przewodnik obejmuje:
- Przegląd platformy Windows AI Foundry i jej komponentów
- API Phi Silica do efektywnego wnioskowania na sprzęcie NPU
- API Computer Vision do przetwarzania obrazów i OCR
- Integrację i optymalizację runtime Windows ML
- Foundry Local CLI do lokalnego rozwoju i testowania
- Strategie optymalizacji sprzętu dla urządzeń Windows
- Praktyczne przykłady implementacji i najlepsze praktyki

### [AI Toolkit do rozwoju Edge AI](./aitoolkit.md)
Dla programistów korzystających z Visual Studio Code, rozszerzenie AI Toolkit zapewnia kompleksowe środowisko rozwoju specjalnie zaprojektowane do budowy, testowania i wdrażania aplikacji Edge AI. Narzędzie to usprawnia cały proces rozwoju Edge AI w VS Code.

**Przewodnik rozwoju**: [AI Toolkit do rozwoju Edge AI](./aitoolkit.md)

Przewodnik AI Toolkit obejmuje:
- Odkrywanie i wybór modeli do wdrożeń brzegowych
- Lokalne testowanie i optymalizacja przepływów pracy
- Integrację ONNX i Ollama dla modeli brzegowych
- Techniki konwersji i kwantyzacji modeli
- Rozwój agentów dla scenariuszy brzegowych
- Ocena wydajności i monitorowanie
- Przygotowanie do wdrożenia i najlepsze praktyki

## Podsumowanie

Te pięć implementacji EdgeAI pokazuje dojrzałość i różnorodność dostępnych dziś rozwiązań Edge AI. Od urządzeń brzegowych przyspieszanych sprzętowo, takich jak Jetson Orin Nano, po frameworki programowe, takie jak ONNX Runtime GenAI i Windows ML, programiści mają niespotykane możliwości wdrażania inteligentnych aplikacji na urządzeniach brzegowych.

Wspólnym elementem wszystkich tych platform jest demokratyzacja możliwości AI, czyniąc zaawansowane uczenie maszynowe dostępne dla programistów o różnych poziomach umiejętności i w różnych zastosowaniach. Niezależnie od tego, czy tworzysz aplikacje mobilne, oprogramowanie desktopowe czy systemy wbudowane, te rozwiązania EdgeAI stanowią fundament dla nowej generacji inteligentnych aplikacji, które działają wydajnie i prywatnie na urządzeniach brzegowych.

Każda platforma oferuje unikalne zalety: Jetson Orin Nano dla przyspieszanego sprzętowo obliczeń brzegowych, ONNX Runtime GenAI dla rozwoju mobilnego na różnych platformach, Azure EdgeAI dla integracji chmura-brzeg na poziomie przedsiębiorstwa, Windows ML dla aplikacji natywnych Windows oraz Foundry Local dla implementacji RAG skoncentrowanych na prywatności. Razem tworzą kompleksowy ekosystem dla rozwoju EdgeAI.

---

