<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c0cb9f7bcff2bc170532d8870a891f38",
  "translation_date": "2025-09-19T00:24:46+00:00",
  "source_file": "Module04/README.md",
  "language_code": "sl"
}
-->
# Poglavje 04: Pretvorba modelov in kvantizacija - Pregled poglavja

Pojav EdgeAI je naredil pretvorbo formatov modelov in kvantizacijo ključni tehnologiji za uvajanje naprednih zmogljivosti strojnega učenja na napravah z omejenimi viri. To poglavje ponuja celovit vodnik za razumevanje, implementacijo in optimizacijo modelov za scenarije uvajanja na robu.

## 📚 Struktura poglavja in učna pot

Poglavje je razdeljeno na šest progresivnih delov, ki se med seboj nadgrajujejo, da ustvarijo celovito razumevanje optimizacije modelov za robno računalništvo:

---

## [Del 1: Osnove pretvorbe formatov modelov in kvantizacije](./01.Introduce.md)

### 🎯 Pregled
Ta uvodni del vzpostavlja teoretični okvir za optimizacijo modelov v okoljih robnega računalništva, pri čemer pokriva meje kvantizacije od 1-bitne do 8-bitne natančnosti ter ključne strategije pretvorbe formatov.

**Ključne teme:**
- Okvir za razvrščanje natančnosti (zelo nizka, nizka, srednja natančnost)
- Prednosti in primeri uporabe formatov GGUF in ONNX
- Koristi kvantizacije za operativno učinkovitost in prilagodljivost uvajanja
- Primerjave zmogljivosti in pomnilniških zahtev

**Učni cilji:**
- Razumeti meje in razvrstitve kvantizacije
- Prepoznati ustrezne tehnike pretvorbe formatov
- Naučiti se naprednih strategij optimizacije za uvajanje na robu

---

## [Del 2: Vodnik za implementacijo Llama.cpp](./02.Llamacpp.md)

### 🎯 Pregled
Celovit vodič za implementacijo Llama.cpp, zmogljivega C++ okvira, ki omogoča učinkovito sklepanje velikih jezikovnih modelov z minimalno nastavitvijo na različnih strojnih konfiguracijah.

**Ključne teme:**
- Namestitev na platformah Windows, macOS in Linux
- Pretvorba formatov GGUF in različne ravni kvantizacije (Q2_K do Q8_0)
- Pospeševanje strojne opreme s CUDA, Metal, OpenCL in Vulkan
- Integracija s Pythonom in strategije za produkcijsko uvajanje

**Učni cilji:**
- Obvladati namestitev na različnih platformah in gradnjo iz izvorne kode
- Implementirati tehnike kvantizacije in optimizacije modelov
- Uvajati modele v strežniškem načinu z integracijo REST API

---

## [Del 3: Microsoft Olive - komplet za optimizacijo](./03.MicrosoftOlive.md)

### 🎯 Pregled
Raziskovanje Microsoft Olive, orodja za optimizacijo modelov, ki upošteva strojno opremo in vključuje več kot 40 vgrajenih komponent za optimizacijo, zasnovanih za uvajanje modelov na ravni podjetja na različnih strojnih platformah.

**Ključne teme:**
- Funkcije samodejne optimizacije z dinamično in statično kvantizacijo
- Inteligenca, ki upošteva strojno opremo, za uvajanje na CPU, GPU in NPU
- Podpora priljubljenim modelom (Llama, Phi, Qwen, Gemma) brez dodatnih nastavitev
- Integracija v podjetniške delovne tokove z Azure ML

**Učni cilji:**
- Izkoristiti samodejno optimizacijo za različne arhitekture modelov
- Implementirati strategije uvajanja na različnih platformah
- Vzpostaviti optimizacijske procese, pripravljene za podjetja

---

## [Del 4: OpenVINO Toolkit - komplet za optimizacijo](./04.openvino.md)

### 🎯 Pregled
Celovito raziskovanje Intelovega orodja OpenVINO, odprtokodne platforme za uvajanje zmogljivih AI rešitev v oblaku, lokalno in na robu, z naprednimi zmogljivostmi okvira za stiskanje nevronskih mrež (NNCF).

**Ključne teme:**
- Uvajanje na različnih platformah s pospeševanjem strojne opreme (CPU, GPU, VPU, AI pospeševalniki)
- Okvir za stiskanje nevronskih mrež (NNCF) za napredno kvantizacijo in obrezovanje
- OpenVINO GenAI za optimizacijo in uvajanje velikih jezikovnih modelov
- Zmogljivosti strežnika modelov za uvajanje na ravni podjetja

**Učni cilji:**
- Obvladati pretvorbo in optimizacijo modelov z OpenVINO
- Implementirati napredne tehnike kvantizacije z NNCF
- Uvajati optimizirane modele na različnih strojnih platformah s strežnikom modelov

---

## [Del 5: Apple MLX Framework - poglobljena analiza](./05.AppleMLX.md)

### 🎯 Pregled
Celovita obravnava Apple MLX, revolucionarnega okvira, posebej zasnovanega za učinkovito strojno učenje na Apple Silicon, s poudarkom na zmogljivostih velikih jezikovnih modelov in lokalnem uvajanju.

**Ključne teme:**
- Prednosti enotne pomnilniške arhitekture in Metal Performance Shaders
- Podpora za modele LLaMA, Mistral, Phi-3, Qwen in Code Llama
- LoRA prilagoditev za učinkovito prilagajanje modelov
- Integracija s Hugging Face in podpora za kvantizacijo (4-bitna in 8-bitna)

**Učni cilji:**
- Obvladati optimizacijo za Apple Silicon pri uvajanju velikih jezikovnih modelov
- Implementirati tehnike prilagoditve in prilagajanja modelov
- Graditi AI aplikacije na ravni podjetja z izboljšanimi funkcijami zasebnosti

---

## [Del 6: Sinteza delovnega toka za razvoj Edge AI](./06.workflow-synthesis.md)

### 🎯 Pregled
Celovita sinteza vseh optimizacijskih okvirov v enotne delovne tokove, odločitvene matrike in najboljše prakse za uvajanje Edge AI, pripravljeno za produkcijo, na različnih platformah in za različne primere uporabe.

**Ključne teme:**
- Enotna arhitektura delovnega toka, ki vključuje več optimizacijskih okvirov
- Odločitvena drevesa za izbiro okvirov in analiza kompromisov zmogljivosti
- Validacija pripravljenosti za produkcijo in celovite strategije uvajanja
- Strategije za prihodnost za nove strojne opreme in arhitekture modelov

**Učni cilji:**
- Obvladati sistematično izbiro okvirov glede na zahteve in omejitve
- Implementirati produkcijske Edge AI procese z obsežnim spremljanjem
- Oblikovati prilagodljive delovne tokove, ki se razvijajo z novimi tehnologijami in zahtevami

---

## 🎯 Učni cilji poglavja

Po zaključku tega celovitega poglavja bodo bralci dosegli:

### **Tehnično znanje**
- Globoko razumevanje meja kvantizacije in praktičnih aplikacij
- Praktične izkušnje z več optimizacijskimi okviri
- Spretnosti za uvajanje v okolja robnega računalništva

### **Strateško razumevanje**
- Sposobnost izbire optimizacij, ki upoštevajo strojno opremo
- Informirano odločanje o kompromisih zmogljivosti
- Strategije za uvajanje in spremljanje na ravni podjetja

### **Primerjalni rezultati**

| Okvir       | Kvantizacija | Uporaba pomnilnika | Izboljšanje hitrosti | Primer uporabe              |
|-------------|-------------|--------------------|----------------------|-----------------------------|
| Llama.cpp   | Q4_K_M      | ~4GB              | 2-3x                | Uvajanje na različnih platformah |
| Olive       | INT4        | Zmanjšanje za 60-75% | 2-6x                | Podjetniški delovni tokovi |
| OpenVINO    | INT8/INT4   | Zmanjšanje za 50-75% | 2-5x                | Optimizacija za Intel strojno opremo |
| MLX         | 4-bit       | ~4GB              | 2-4x                | Optimizacija za Apple Silicon |

## 🚀 Naslednji koraki in napredne aplikacije

To poglavje ponuja celovito osnovo za:
- Razvoj prilagojenih modelov za specifična področja
- Raziskave na področju optimizacije Edge AI
- Razvoj komercialnih AI aplikacij
- Uvajanje Edge AI na ravni podjetja v velikem obsegu

Znanje iz teh šestih delov ponuja celovit nabor orodij za navigacijo po hitro razvijajočem se področju optimizacije in uvajanja modelov Edge AI.

---

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitna napačna razumevanja ali napačne interpretacije, ki bi nastale zaradi uporabe tega prevoda.