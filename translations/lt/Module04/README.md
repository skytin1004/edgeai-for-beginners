<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-19T00:26:03+00:00",
  "source_file": "Module04/README.md",
  "language_code": "lt"
}
-->
# 4 skyrius: Modelių formato konvertavimas ir kvantizavimas – skyrius apžvalga

EdgeAI atsiradimas padarė modelių formato konvertavimą ir kvantizavimą esminėmis technologijomis, leidžiančiomis diegti pažangias mašininio mokymosi galimybes ribotų resursų įrenginiuose. Šis išsamus skyrius pateikia pilną vadovą, kaip suprasti, įgyvendinti ir optimizuoti modelius, skirtus diegimui kraštiniuose scenarijuose.

## 📚 Skyriaus struktūra ir mokymosi kelias

Šis skyrius suskirstytas į šešias progresyvias dalis, kurios viena kitą papildo, siekiant sukurti išsamų modelių optimizavimo kraštiniam kompiuterijos supratimą:

---

## [1 dalis: Modelių formato konvertavimo ir kvantizavimo pagrindai](./01.Introduce.md)

### 🎯 Apžvalga
Ši pagrindinė dalis nustato teorinį pagrindą modelių optimizavimui kraštiniuose kompiuterijos aplinkose, apimant kvantizavimo ribas nuo 1-bit iki 8-bit tikslumo lygių ir pagrindines formato konvertavimo strategijas.

**Pagrindinės temos:**
- Tikslumo klasifikavimo sistema (itin žemas, žemas, vidutinis tikslumas)
- GGUF ir ONNX formato privalumai ir naudojimo atvejai
- Kvantizavimo nauda operaciniam efektyvumui ir diegimo lankstumui
- Našumo palyginimai ir atminties naudojimo skirtumai

**Mokymosi rezultatai:**
- Suprasti kvantizavimo ribas ir klasifikacijas
- Identifikuoti tinkamas formato konvertavimo technikas
- Išmokti pažangias optimizavimo strategijas kraštiniam diegimui

---

## [2 dalis: Llama.cpp įgyvendinimo vadovas](./02.Llamacpp.md)

### 🎯 Apžvalga
Išsamus vadovas, kaip įgyvendinti Llama.cpp – galingą C++ sistemą, leidžiančią efektyviai vykdyti didelius kalbos modelius su minimaliu nustatymu įvairiose aparatinės įrangos konfigūracijose.

**Pagrindinės temos:**
- Diegimas Windows, macOS ir Linux platformose
- GGUF formato konvertavimas ir įvairūs kvantizavimo lygiai (Q2_K iki Q8_0)
- Aparatinės įrangos pagreitinimas naudojant CUDA, Metal, OpenCL ir Vulkan
- Python integracija ir diegimo strategijos gamybai

**Mokymosi rezultatai:**
- Įvaldyti diegimą įvairiose platformose ir kūrimą iš šaltinio
- Įgyvendinti modelių kvantizavimo ir optimizavimo technikas
- Diegti modelius serverio režimu su REST API integracija

---

## [3 dalis: Microsoft Olive optimizavimo rinkinys](./03.MicrosoftOlive.md)

### 🎯 Apžvalga
Microsoft Olive tyrinėjimas – aparatinės įrangos optimizavimo įrankių rinkinys su daugiau nei 40 integruotų optimizavimo komponentų, skirtas įmonės lygio modelių diegimui įvairiose aparatinės įrangos platformose.

**Pagrindinės temos:**
- Automatinės optimizavimo funkcijos su dinamišku ir statiniu kvantizavimu
- Aparatinės įrangos intelektas CPU, GPU ir NPU diegimui
- Populiarių modelių palaikymas (Llama, Phi, Qwen, Gemma) iš karto
- Įmonės integracija su Azure ML ir gamybos darbo eigomis

**Mokymosi rezultatai:**
- Pasinaudoti automatine optimizacija įvairioms modelių architektūroms
- Įgyvendinti diegimo strategijas įvairiose platformose
- Sukurti įmonės lygio optimizavimo procesus

---

## [4 dalis: OpenVINO įrankių rinkinio optimizavimo rinkinys](./04.openvino.md)

### 🎯 Apžvalga
Išsamus Intel OpenVINO įrankių rinkinio tyrinėjimas – atviro kodo platforma, skirta diegti efektyvius AI sprendimus debesyje, vietoje ir kraštiniuose aplinkose su pažangiomis Neural Network Compression Framework (NNCF) galimybėmis.

**Pagrindinės temos:**
- Diegimas įvairiose platformose su aparatinės įrangos pagreitinimu (CPU, GPU, VPU, AI akceleratoriai)
- Neural Network Compression Framework (NNCF) pažangiam kvantizavimui ir genėjimui
- OpenVINO GenAI didelių kalbos modelių optimizavimui ir diegimui
- Įmonės lygio modelių serverio galimybės ir mastelio diegimo strategijos

**Mokymosi rezultatai:**
- Įvaldyti OpenVINO modelių konvertavimo ir optimizavimo darbo eigas
- Įgyvendinti pažangias kvantizavimo technikas su NNCF
- Diegti optimizuotus modelius įvairiose aparatinės įrangos platformose su Model Server

---

## [5 dalis: Apple MLX sistemos giluminė analizė](./05.AppleMLX.md)

### 🎯 Apžvalga
Išsamus Apple MLX tyrinėjimas – revoliucinė sistema, specialiai sukurta efektyviam mašininio mokymosi vykdymui Apple Silicon, akcentuojant didelių kalbos modelių galimybes ir vietinį diegimą.

**Pagrindinės temos:**
- Vieningos atminties architektūros privalumai ir Metal Performance Shaders
- LLaMA, Mistral, Phi-3, Qwen ir Code Llama modelių palaikymas
- LoRA smulkus derinimas efektyviam modelių pritaikymui
- Hugging Face integracija ir kvantizavimo palaikymas (4-bit ir 8-bit)

**Mokymosi rezultatai:**
- Įvaldyti Apple Silicon optimizavimą LLM diegimui
- Įgyvendinti smulkaus derinimo ir modelių pritaikymo technikas
- Kurti įmonės AI programas su patobulintomis privatumo funkcijomis

---

## [6 dalis: Edge AI kūrimo darbo eigos sintezė](./06.workflow-synthesis.md)

### 🎯 Apžvalga
Išsamus visų optimizavimo sistemų sintezavimas į vieningas darbo eigas, sprendimų matricas ir geriausias praktikas, skirtas gamybai paruoštam Edge AI diegimui įvairiose platformose ir naudojimo atvejais.

**Pagrindinės temos:**
- Vieninga darbo eigos architektūra, integruojanti kelias optimizavimo sistemas
- Sistemos pasirinkimo sprendimų medžiai ir našumo kompromisų analizė
- Gamybos pasirengimo validacija ir išsamios diegimo strategijos
- Ateities strategijos naujai atsirandančiai aparatinės įrangai ir modelių architektūroms

**Mokymosi rezultatai:**
- Įvaldyti sistemingą sistemos pasirinkimą pagal reikalavimus ir apribojimus
- Įgyvendinti gamybos lygio Edge AI procesus su išsamia stebėsena
- Kurti pritaikomas darbo eigas, kurios evoliucionuoja kartu su naujomis technologijomis ir reikalavimais

---

## 🎯 Skyriaus mokymosi rezultatai

Baigus šį išsamų skyrių, skaitytojai pasieks:

### **Techninį meistriškumą**
- Gilų kvantizavimo ribų ir praktinių pritaikymų supratimą
- Praktinę patirtį su įvairiomis optimizavimo sistemomis
- Gamybos diegimo įgūdžius kraštiniuose kompiuterijos aplinkose

### **Strateginį supratimą**
- Aparatinės įrangos optimizavimo pasirinkimo galimybes
- Informuotą sprendimų priėmimą dėl našumo kompromisų
- Įmonės lygio diegimo ir stebėjimo strategijas

### **Našumo palyginimai**

| Sistema     | Kvantizavimas | Atminties naudojimas | Greičio padidėjimas | Naudojimo atvejis              |
|-------------|---------------|----------------------|---------------------|--------------------------------|
| Llama.cpp   | Q4_K_M        | ~4GB                | 2-3x               | Diegimas įvairiose platformose |
| Olive       | INT4          | 60-75% mažinimas    | 2-6x               | Įmonės darbo eigos             |
| OpenVINO    | INT8/INT4     | 50-75% mažinimas    | 2-5x               | Intel aparatinės įrangos optimizavimas |
| MLX         | 4-bit         | ~4GB                | 2-4x               | Apple Silicon optimizavimas    |

## 🚀 Kiti žingsniai ir pažangios taikymo galimybės

Šis skyrius suteikia pilną pagrindą:
- Individualių modelių kūrimui specifinėms sritims
- Tyrimams Edge AI optimizavimo srityje
- Komercinių AI programų kūrimui
- Didelio masto įmonės Edge AI diegimams

Žinios iš šių šešių dalių siūlo išsamų įrankių rinkinį, skirtą naviguoti sparčiai besikeičiančiame Edge AI modelių optimizavimo ir diegimo kraštovaizdyje.

---

**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama profesionali žmogaus vertimo paslauga. Mes neprisiimame atsakomybės už nesusipratimus ar klaidingus interpretavimus, atsiradusius naudojant šį vertimą.