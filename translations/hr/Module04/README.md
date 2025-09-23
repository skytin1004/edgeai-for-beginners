<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-19T00:24:20+00:00",
  "source_file": "Module04/README.md",
  "language_code": "hr"
}
-->
# Poglavlje 04: Pretvorba formata modela i kvantizacija - Pregled poglavlja

Pojava EdgeAI-a učinila je pretvorbu formata modela i kvantizaciju ključnim tehnologijama za implementaciju naprednih mogućnosti strojnog učenja na uređajima s ograničenim resursima. Ovo sveobuhvatno poglavlje pruža potpuni vodič za razumijevanje, implementaciju i optimizaciju modela za scenarije implementacije na rubnim uređajima.

## 📚 Struktura poglavlja i put učenja

Ovo poglavlje organizirano je u šest progresivnih sekcija, od kojih svaka nadograđuje prethodnu kako bi se stvorilo sveobuhvatno razumijevanje optimizacije modela za rubno računalstvo:

---

## [Sekcija 1: Osnove pretvorbe formata modela i kvantizacije](./01.Introduce.md)

### 🎯 Pregled
Ova temeljna sekcija postavlja teorijski okvir za optimizaciju modela u okruženjima rubnog računalstva, pokrivajući granice kvantizacije od 1-bitne do 8-bitne preciznosti te ključne strategije pretvorbe formata.

**Ključne teme:**
- Okvir za klasifikaciju preciznosti (ultra-niska, niska, srednja preciznost)
- Prednosti i primjene GGUF i ONNX formata
- Prednosti kvantizacije za operativnu učinkovitost i fleksibilnost implementacije
- Usporedbe performansi i memorijskog otiska

**Ishodi učenja:**
- Razumjeti granice i klasifikacije kvantizacije
- Identificirati odgovarajuće tehnike pretvorbe formata
- Naučiti napredne strategije optimizacije za implementaciju na rubnim uređajima

---

## [Sekcija 2: Vodič za implementaciju Llama.cpp](./02.Llamacpp.md)

### 🎯 Pregled
Sveobuhvatan vodič za implementaciju Llama.cpp, moćnog C++ okvira koji omogućuje učinkovitu inferenciju velikih jezičnih modela uz minimalnu postavku na raznim hardverskim konfiguracijama.

**Ključne teme:**
- Instalacija na Windows, macOS i Linux platformama
- Pretvorba u GGUF format i različite razine kvantizacije (Q2_K do Q8_0)
- Hardverska akceleracija s CUDA, Metal, OpenCL i Vulkan
- Integracija s Pythonom i strategije za produkcijsku implementaciju

**Ishodi učenja:**
- Ovladati instalacijom na više platformi i izgradnjom iz izvornog koda
- Implementirati tehnike kvantizacije i optimizacije modela
- Implementirati modele u server modu s REST API integracijom

---

## [Sekcija 3: Microsoft Olive alat za optimizaciju](./03.MicrosoftOlive.md)

### 🎯 Pregled
Istraživanje Microsoft Olive-a, alata za optimizaciju modela svjesnog hardvera s više od 40 ugrađenih komponenti za optimizaciju, dizajniranog za implementaciju modela na raznim hardverskim platformama na razini poduzeća.

**Ključne teme:**
- Automatske značajke optimizacije s dinamičkom i statičkom kvantizacijom
- Inteligencija svjesna hardvera za implementaciju na CPU, GPU i NPU
- Podrška za popularne modele (Llama, Phi, Qwen, Gemma) bez dodatne konfiguracije
- Integracija na razini poduzeća s Azure ML i produkcijskim tijekovima rada

**Ishodi učenja:**
- Iskoristiti automatiziranu optimizaciju za različite arhitekture modela
- Implementirati strategije implementacije na više platformi
- Uspostaviti optimizacijske procese spremne za poduzeće

---

## [Sekcija 4: OpenVINO alat za optimizaciju](./04.openvino.md)

### 🎯 Pregled
Sveobuhvatno istraživanje Intelovog OpenVINO alata, otvorene platforme za implementaciju učinkovitih AI rješenja u oblaku, lokalno i na rubnim uređajima s naprednim mogućnostima okvira za kompresiju neuronskih mreža (NNCF).

**Ključne teme:**
- Implementacija na više platformi s hardverskom akceleracijom (CPU, GPU, VPU, AI akceleratori)
- Okvir za kompresiju neuronskih mreža (NNCF) za naprednu kvantizaciju i obrezivanje
- OpenVINO GenAI za optimizaciju i implementaciju velikih jezičnih modela
- Mogućnosti model servera na razini poduzeća i skalabilne strategije implementacije

**Ishodi učenja:**
- Ovladati procesima pretvorbe i optimizacije modela s OpenVINO alatom
- Implementirati napredne tehnike kvantizacije s NNCF-om
- Implementirati optimizirane modele na raznim hardverskim platformama uz Model Server

---

## [Sekcija 5: Detaljno istraživanje Apple MLX okvira](./05.AppleMLX.md)

### 🎯 Pregled
Sveobuhvatno pokrivanje Apple MLX-a, revolucionarnog okvira posebno dizajniranog za učinkovito strojno učenje na Apple Siliconu, s naglaskom na mogućnosti velikih jezičnih modela i lokalnu implementaciju.

**Ključne teme:**
- Prednosti arhitekture unificirane memorije i Metal Performance Shaders
- Podrška za modele LLaMA, Mistral, Phi-3, Qwen i Code Llama
- LoRA fino podešavanje za učinkovitu prilagodbu modela
- Integracija s Hugging Face-om i podrška za kvantizaciju (4-bitna i 8-bitna)

**Ishodi učenja:**
- Ovladati optimizacijom za Apple Silicon za implementaciju velikih jezičnih modela
- Implementirati tehnike fino podešavanja i prilagodbe modela
- Izgraditi AI aplikacije na razini poduzeća s poboljšanim značajkama privatnosti

---

## [Sekcija 6: Sinteza tijeka rada za razvoj Edge AI-a](./06.workflow-synthesis.md)

### 🎯 Pregled
Sveobuhvatna sinteza svih okvira za optimizaciju u jedinstvene tijekove rada, matrice odluka i najbolje prakse za implementaciju Edge AI-a spremnog za produkciju na raznim platformama i za različite primjene.

**Ključne teme:**
- Jedinstvena arhitektura tijeka rada koja integrira više okvira za optimizaciju
- Stabla odluka za odabir okvira i analiza kompromisa u performansama
- Validacija spremnosti za produkciju i sveobuhvatne strategije implementacije
- Strategije za buduću prilagodbu novim hardverskim i modelskim arhitekturama

**Ishodi učenja:**
- Ovladati sustavnim odabirom okvira na temelju zahtjeva i ograničenja
- Implementirati produkcijske Edge AI procese s cjelovitim praćenjem
- Dizajnirati prilagodljive tijekove rada koji se razvijaju s novim tehnologijama i zahtjevima

---

## 🎯 Ishodi učenja poglavlja

Nakon završetka ovog sveobuhvatnog poglavlja, čitatelji će postići:

### **Tehničko znanje**
- Duboko razumijevanje granica kvantizacije i praktičnih primjena
- Praktično iskustvo s više okvira za optimizaciju
- Vještine za produkcijsku implementaciju u rubnim računalnim okruženjima

### **Strateško razumijevanje**
- Sposobnost odabira optimizacije svjesne hardvera
- Informirano donošenje odluka o kompromisima u performansama
- Strategije za implementaciju i praćenje na razini poduzeća

### **Usporedbe performansi**

| Okvir       | Kvantizacija | Korištenje memorije | Poboljšanje brzine | Primjena                     |
|-------------|--------------|---------------------|--------------------|------------------------------|
| Llama.cpp   | Q4_K_M       | ~4GB               | 2-3x              | Implementacija na više platformi |
| Olive       | INT4         | Smanjenje 60-75%   | 2-6x              | Tijekovi rada na razini poduzeća |
| OpenVINO    | INT8/INT4    | Smanjenje 50-75%   | 2-5x              | Optimizacija za Intel hardver |
| MLX         | 4-bit        | ~4GB               | 2-4x              | Optimizacija za Apple Silicon |

## 🚀 Sljedeći koraci i napredne primjene

Ovo poglavlje pruža potpunu osnovu za:
- Razvoj prilagođenih modela za specifične domene
- Istraživanje u optimizaciji Edge AI-a
- Razvoj komercijalnih AI aplikacija
- Implementaciju Edge AI-a na velikoj skali u poduzećima

Znanje iz ovih šest sekcija nudi sveobuhvatan alat za navigaciju kroz brzo razvijajući krajolik optimizacije i implementacije modela za Edge AI.

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.