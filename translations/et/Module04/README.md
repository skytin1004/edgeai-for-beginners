<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-10-11T11:42:25+00:00",
  "source_file": "Module04/README.md",
  "language_code": "et"
}
-->
# 4. peatükk: Mudelite formaadi konverteerimine ja kvantiseerimine - peatüki ülevaade

EdgeAI esiletõus on muutnud mudelite formaadi konverteerimise ja kvantiseerimise hädavajalikeks tehnoloogiateks, et rakendada keerukaid masinõppevõimalusi piiratud ressurssidega seadmetes. See põhjalik peatükk pakub täielikku juhendit mudelite mõistmiseks, rakendamiseks ja optimeerimiseks serva juurutamise stsenaariumide jaoks.

## 📚 Peatüki struktuur ja õpitee

See peatükk on jaotatud kuueks järjestikuseks osaks, millest igaüks tugineb eelmisele, et luua terviklik arusaam mudelite optimeerimisest servaarvutuse jaoks:

---

## [1. osa: Mudelite formaadi konverteerimise ja kvantiseerimise alused](./01.Introduce.md)

### 🎯 Ülevaade
See sissejuhatav osa loob teoreetilise raamistiku mudelite optimeerimiseks servaarvutuse keskkondades, hõlmates kvantiseerimise piire 1-bitist kuni 8-bitise täpsuseni ja peamisi formaadi konverteerimise strateegiaid.

**Peamised teemad:**
- Täpsuse klassifitseerimise raamistik (väga madal, madal, keskmine täpsus)
- GGUF ja ONNX formaadi eelised ja kasutusjuhtumid
- Kvantiseerimise eelised tööefektiivsuse ja juurutamise paindlikkuse osas
- Jõudlusnäitajad ja mälukasutuse võrdlused

**Õpitulemused:**
- Mõista kvantiseerimise piire ja klassifikatsioone
- Tuvastada sobivad formaadi konverteerimise tehnikad
- Õppida edasijõudnud optimeerimisstrateegiaid serva juurutamiseks

---

## [2. osa: Llama.cpp rakendamise juhend](./02.Llamacpp.md)

### 🎯 Ülevaade
Põhjalik juhend Llama.cpp rakendamiseks, mis on võimas C++ raamistik, mis võimaldab tõhusat suurte keelemudelite järeldamist minimaalse seadistusega erinevates riistvarakonfiguratsioonides.

**Peamised teemad:**
- Installatsioon Windowsi, macOS-i ja Linuxi platvormidel
- GGUF formaadi konverteerimine ja erinevad kvantiseerimistasemed (Q2_K kuni Q8_0)
- Riistvarakiirendus CUDA, Metal, OpenCL ja Vulkan abil
- Pythoni integreerimine ja tootmisesse juurutamise strateegiad

**Õpitulemused:**
- Omandada platvormideülene installatsioon ja allikast kompileerimine
- Rakendada mudelite kvantiseerimise ja optimeerimise tehnikaid
- Juurutada mudeleid serverirežiimis REST API integreerimisega

---

## [3. osa: Microsoft Olive optimeerimiskomplekt](./03.MicrosoftOlive.md)

### 🎯 Ülevaade
Microsoft Olive'i uurimine, mis on riistvarateadlik mudelite optimeerimise tööriistakomplekt, millel on üle 40 sisseehitatud optimeerimiskomponendi ja mis on mõeldud ettevõtte tasemel mudelite juurutamiseks erinevatel riistvaraplatvormidel.

**Peamised teemad:**
- Automaatse optimeerimise funktsioonid dünaamilise ja staatilise kvantiseerimisega
- Riistvarateadlikkus CPU, GPU ja NPU juurutamiseks
- Populaarsete mudelite (Llama, Phi, Qwen, Gemma) tugi
- Ettevõtte integratsioon Azure ML-i ja tootmisvoogudega

**Õpitulemused:**
- Kasutada automaatset optimeerimist erinevate mudeliarhitektuuride jaoks
- Rakendada platvormideüleseid juurutamisstrateegiaid
- Luua ettevõtte tasemel optimeerimisprotsesse

---

## [4. osa: OpenVINO Toolkit optimeerimiskomplekt](./04.openvino.md)

### 🎯 Ülevaade
Põhjalik ülevaade Inteli OpenVINO tööriistakomplektist, mis on avatud lähtekoodiga platvorm, mis võimaldab jõudluslikke tehisintellekti lahendusi pilves, kohapeal ja servakeskkondades, kasutades täiustatud närvivõrkude tihendamise raamistikku (NNCF).

**Peamised teemad:**
- Platvormideülene juurutamine riistvarakiirendusega (CPU, GPU, VPU, AI kiirendid)
- Närvivõrkude tihendamise raamistik (NNCF) edasijõudnud kvantiseerimise ja kärpimise jaoks
- OpenVINO GenAI suurte keelemudelite optimeerimiseks ja juurutamiseks
- Ettevõtte tasemel mudeliserveri võimalused ja skaleeritavad juurutamisstrateegiad

**Õpitulemused:**
- Omandada OpenVINO mudelite konverteerimise ja optimeerimise töövood
- Rakendada edasijõudnud kvantiseerimistehnikaid NNCF-iga
- Juurutada optimeeritud mudeleid erinevatel riistvaraplatvormidel mudeliserveri abil

---

## [5. osa: Apple MLX raamistik põhjalikult](./05.AppleMLX.md)

### 🎯 Ülevaade
Põhjalik ülevaade Apple MLX-ist, revolutsioonilisest raamistikust, mis on spetsiaalselt loodud tõhusaks masinõppeks Apple Siliconil, keskendudes suurte keelemudelite võimalustele ja kohalikule juurutamisele.

**Peamised teemad:**
- Ühtse mälustruktuuri eelised ja Metal Performance Shaders
- Tugi LLaMA, Mistral, Phi-3, Qwen ja Code Llama mudelitele
- LoRA peenhäälestus tõhusaks mudelite kohandamiseks
- Hugging Face integratsioon ja kvantiseerimise tugi (4-bitine ja 8-bitine)

**Õpitulemused:**
- Omandada Apple Siliconi optimeerimine suurte keelemudelite juurutamiseks
- Rakendada peenhäälestus- ja mudelite kohandamistehnikaid
- Luua ettevõtte tehisintellekti rakendusi täiustatud privaatsusfunktsioonidega

---

## [6. osa: Edge AI arendustöövoo süntees](./06.workflow-synthesis.md)

### 🎯 Ülevaade
Kõigi optimeerimisraamistike põhjalik süntees ühtseteks töövoogudeks, otsustusmaatriksiteks ja parimateks praktikuteks tootmisvalmis Edge AI juurutamiseks erinevatel platvormidel ja kasutusjuhtudel.

**Peamised teemad:**
- Ühtne töövoo arhitektuur, mis integreerib mitmeid optimeerimisraamistikke
- Raamistiku valiku otsustuspuud ja jõudluse kompromisside analüüs
- Tootmisvalmiduse valideerimine ja põhjalikud juurutamisstrateegiad
- Tulevikukindlad strateegiad uute riistvara ja mudeliarhitektuuride jaoks

**Õpitulemused:**
- Omandada süstemaatiline raamistik valikute tegemiseks vastavalt nõuetele ja piirangutele
- Rakendada tootmiskõlblikke Edge AI töövooge koos põhjaliku jälgimisega
- Kujundada kohandatavaid töövooge, mis arenevad koos uute tehnoloogiate ja nõuetega

---

## 🎯 Peatüki õpitulemused

Pärast selle põhjaliku peatüki läbimist saavutavad lugejad:

### **Tehniline meisterlikkus**
- Sügav arusaam kvantiseerimise piiridest ja praktilistest rakendustest
- Praktiline kogemus mitme optimeerimisraamistikuga
- Tootmisesse juurutamise oskused servaarvutuse keskkondades

### **Strateegiline arusaam**
- Riistvarateadlik optimeerimise valikuvõimekus
- Informeeritud otsuste tegemine jõudluse kompromisside osas
- Ettevõtte tasemel juurutamise ja jälgimise strateegiad

### **Jõudlusnäitajad**

| Raamistik | Kvantiseerimine | Mälukasutus | Kiiruse paranemine | Kasutusjuhtum |
|-----------|-----------------|-------------|--------------------|---------------|
| Llama.cpp | Q4_K_M          | ~4GB        | 2-3x               | Platvormideülene juurutamine |
| Olive     | INT4            | 60-75% vähenemine | 2-6x         | Ettevõtte töövood |
| OpenVINO  | INT8/INT4       | 50-75% vähenemine | 2-5x         | Inteli riistvara optimeerimine |
| MLX       | 4-bitine        | ~4GB        | 2-4x               | Apple Siliconi optimeerimine |

## 🚀 Järgmised sammud ja edasijõudnud rakendused

See peatükk pakub täielikku alust:
- Kohandatud mudelite arendamiseks spetsiifilistele valdkondadele
- Uurimistööks serva tehisintellekti optimeerimise alal
- Kaubanduslike tehisintellekti rakenduste arendamiseks
- Suuremahuliste ettevõtte serva tehisintellekti juurutuste jaoks

Nende kuue osa teadmised pakuvad terviklikku tööriistakomplekti, et navigeerida kiiresti arenevas serva tehisintellekti mudelite optimeerimise ja juurutamise maastikus.

---

**Lahtiütlus**:  
See dokument on tõlgitud AI tõlketeenuse [Co-op Translator](https://github.com/Azure/co-op-translator) abil. Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algne dokument selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valesti tõlgenduste eest.