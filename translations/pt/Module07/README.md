<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cb6eadc312d5658a0cd71c0085b43742",
  "translation_date": "2025-09-22T12:37:19+00:00",
  "source_file": "Module07/README.md",
  "language_code": "pt"
}
-->
# Capítulo 07: Exemplos de EdgeAI

Edge AI representa a convergência da inteligência artificial com a computação de borda, permitindo o processamento inteligente diretamente nos dispositivos, sem depender de conectividade com a nuvem. Este capítulo explora cinco implementações distintas de EdgeAI em diferentes plataformas e frameworks, demonstrando a versatilidade e o poder de executar modelos de IA na borda.

## 1. EdgeAI no NVIDIA Jetson Orin Nano

O NVIDIA Jetson Orin Nano representa um avanço na computação de IA de borda acessível, oferecendo até 67 TOPS de desempenho de IA em um formato compacto, do tamanho de um cartão de crédito. Esta poderosa plataforma de IA de borda democratiza o desenvolvimento de IA generativa para entusiastas, estudantes e desenvolvedores profissionais.

### Principais Características
- Oferece até 67 TOPS de desempenho de IA — uma melhoria de 1,7X em relação ao seu antecessor
- 1024 núcleos CUDA e até 32 Tensor Cores para processamento de IA
- CPU Arm Cortex-A78AE v8.2 de 6 núcleos e 64 bits com frequência máxima de 1,5 GHz
- Preço de apenas $249, proporcionando a desenvolvedores, estudantes e criadores a plataforma mais acessível e econômica

### Aplicações
O Jetson Orin Nano destaca-se na execução de modelos modernos de IA generativa, incluindo transformadores de visão, grandes modelos de linguagem e modelos de visão-linguagem. Foi projetado especificamente para casos de uso de GenAI e agora é possível executar vários LLMs em um dispositivo do tamanho da palma da mão. Casos de uso populares incluem robótica com IA, drones inteligentes, câmaras inteligentes e dispositivos autónomos de borda.

**Saiba Mais**: [Supercomputador Jetson Orin Nano da NVIDIA: A Próxima Grande Inovação em EdgeAI](https://medium.com/data-science-in-your-pocket/nvidias-jetson-orin-nano-supercomputer-the-next-big-thing-in-edgeai-e9eff687ae62)

## 2. EdgeAI em Aplicações Móveis com .NET MAUI e ONNX Runtime GenAI

Esta solução demonstra como integrar IA Generativa e Grandes Modelos de Linguagem (LLMs) em aplicações móveis multiplataforma usando .NET MAUI (Interface de Aplicação Multiplataforma) e ONNX Runtime GenAI. Esta abordagem permite que desenvolvedores .NET criem aplicações móveis sofisticadas com IA que funcionam nativamente em dispositivos Android e iOS.

### Principais Características
- Baseado no framework .NET MAUI, fornecendo uma única base de código para aplicações Android e iOS
- Integração com ONNX Runtime GenAI para executar modelos de IA generativa diretamente em dispositivos móveis
- Suporte a vários aceleradores de hardware adaptados para dispositivos móveis, incluindo CPU, GPU e processadores de IA especializados
- Otimizações específicas para plataformas, como CoreML para iOS e NNAPI para Android, através do ONNX Runtime
- Implementa o ciclo completo de IA generativa, incluindo pré e pós-processamento, inferência, processamento de logits, pesquisa e amostragem, e gestão de cache KV

### Benefícios para Desenvolvedores
A abordagem .NET MAUI permite que os desenvolvedores aproveitem suas habilidades existentes em C# e .NET enquanto criam aplicações de IA multiplataforma. O framework ONNX Runtime GenAI suporta várias arquiteturas de modelos, incluindo Llama, Mistral, Phi, Gemma e muitas outras. Kernels ARM64 otimizados aceleram a multiplicação de matrizes quantizadas em INT4, garantindo desempenho eficiente em hardware móvel, mantendo a experiência familiar de desenvolvimento em .NET.

### Casos de Uso
Esta solução é ideal para desenvolvedores que desejam criar aplicações móveis com IA usando tecnologias .NET, incluindo chatbots inteligentes, aplicações de reconhecimento de imagem, ferramentas de tradução de idiomas e sistemas de recomendação personalizados que funcionam inteiramente no dispositivo, garantindo maior privacidade e capacidade offline.

**Saiba Mais**: [Exemplo de .NET MAUI ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai/tree/jialli/genny-maui/examples/csharp/GennyMaui)

## 3. EdgeAI no Azure com Motor de Modelos de Linguagem Pequenos

A solução EdgeAI baseada no Azure da Microsoft foca na implementação eficiente de Modelos de Linguagem Pequenos (SLMs) em ambientes híbridos de nuvem e borda. Esta abordagem conecta os serviços de IA em escala de nuvem às necessidades de implementação na borda.

### Vantagens da Arquitetura
- Integração perfeita com serviços de IA do Azure
- Executa SLMs/LLMs e modelos multimodais no dispositivo e na nuvem com ONNX Runtime
- Otimizado para implementações em escala empresarial
- Suporte para atualizações e gestão contínua de modelos

### Casos de Uso
A implementação do Azure EdgeAI destaca-se em cenários que exigem implementações de IA em nível empresarial com capacidades de gestão na nuvem. Isso inclui processamento inteligente de documentos, análises em tempo real e fluxos de trabalho híbridos de IA que aproveitam recursos de computação na nuvem e na borda.

**Saiba Mais**: [Motor de SLM do Azure EdgeAI](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/slm_engine)

## 4. EdgeAI com Windows ML

O Windows ML representa o runtime avançado da Microsoft, otimizado para inferência de modelos no dispositivo e implementação simplificada, servindo como a base do Windows AI Foundry. Esta plataforma permite que desenvolvedores criem aplicações Windows com IA que aproveitam todo o potencial do hardware de PC.

### Capacidades da Plataforma
- Funciona em todos os PCs com Windows 11 executando a versão 24H2 (build 26100) ou superior
- Compatível com todo o hardware de PC x64 e ARM64, mesmo PCs sem NPUs ou GPUs
- Permite que os desenvolvedores utilizem seus próprios modelos e os implementem de forma eficiente no ecossistema de parceiros de silício, incluindo AMD, Intel, NVIDIA e Qualcomm, abrangendo CPU, GPU e NPU
- Com APIs de infraestrutura, os desenvolvedores não precisam mais criar várias versões de suas aplicações para diferentes tipos de hardware

### Benefícios para Desenvolvedores
O Windows ML abstrai o hardware e os provedores de execução, permitindo que você se concentre em escrever seu código. Além disso, o Windows ML atualiza-se automaticamente para suportar as NPUs, GPUs e CPUs mais recentes à medida que são lançadas. A plataforma oferece um framework unificado para o desenvolvimento de IA em todo o ecossistema diversificado de hardware do Windows.

**Saiba Mais**: 
- [Visão Geral do Windows ML](https://learn.microsoft.com/en-us/windows/ai/new-windows-ml/overview)
- [Guia de Desenvolvimento de EdgeAI no Windows](../windowdeveloper.md) - Guia abrangente para desenvolvimento de Edge AI no Windows

## 5. EdgeAI com Aplicações Locais do Foundry

O Foundry Local permite que desenvolvedores criem aplicações de Geração Aumentada por Recuperação (RAG) usando recursos locais em .NET, combinando modelos de linguagem locais com capacidades de busca semântica. Esta abordagem oferece soluções de IA focadas na privacidade, operando inteiramente em infraestrutura local.

### Arquitetura Técnica
- Combina o modelo de linguagem Phi, Embeddings Locais e o Kernel Semântico para criar um cenário RAG
- Utiliza embeddings como vetores (arrays) de valores de ponto flutuante que representam conteúdo e seu significado semântico
- O Kernel Semântico atua como o principal orquestrador, integrando Phi e Componentes Inteligentes para criar um pipeline RAG contínuo
- Suporte para bases de dados vetoriais locais, incluindo SQLite e Qdrant

### Benefícios da Implementação
RAG, ou Geração Aumentada por Recuperação, é apenas uma forma sofisticada de dizer "procurar informações e colocá-las no prompt". Esta implementação local garante privacidade de dados enquanto fornece respostas inteligentes baseadas em bases de conhecimento personalizadas. A abordagem é particularmente valiosa para cenários empresariais que exigem soberania de dados e capacidades de operação offline.

**Saiba Mais**: [Exemplos de RAG Local do Foundry](https://github.com/microsoft/Foundry-Local/tree/main/samples/dotNET/rag)

### Foundry Local no Windows

O Microsoft Foundry Local fornece um servidor REST compatível com OpenAI, alimentado pelo ONNX Runtime, para executar modelos localmente no Windows. Abaixo está um resumo rápido e validado; consulte a documentação oficial para detalhes completos.

- Comece aqui: https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started
- Arquitetura: https://learn.microsoft.com/azure/ai-foundry/foundry-local/concepts/foundry-local-architecture
- Referência CLI: https://learn.microsoft.com/azure/ai-foundry/foundry-local/reference/reference-cli
- Guia completo para Windows neste repositório: [foundrylocal.md](./foundrylocal.md)

Instale ou atualize no Windows (cmd.exe):
```cmd
winget install Microsoft.FoundryLocal
winget upgrade --id Microsoft.FoundryLocal
foundry --version
```

Explore categorias do CLI:
```cmd
foundry model --help
foundry service --help
foundry cache --help
```

Execute um modelo e descubra o endpoint dinâmico:
```cmd
foundry model run gpt-oss-20b
foundry service status
```

Verificação rápida do REST para listar modelos (substitua PORT pelo status):
```cmd
curl -s http://localhost:PORT/v1/models
```

Dicas:
- Integração com SDK: https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-integrate-with-inference-sdks
- Traga seu próprio modelo (compile): https://learn.microsoft.com/azure/ai-foundry/foundry-local/how-to/how-to-compile-hugging-face-models

## Recursos de Desenvolvimento de EdgeAI no Windows

Para desenvolvedores que têm como alvo especificamente a plataforma Windows, criámos um guia abrangente que cobre todo o ecossistema de EdgeAI no Windows. Este recurso fornece informações detalhadas sobre o Windows AI Foundry, incluindo APIs, ferramentas e melhores práticas para o desenvolvimento de EdgeAI no Windows.

### Plataforma Windows AI Foundry
A plataforma Windows AI Foundry oferece um conjunto abrangente de ferramentas e APIs projetadas especificamente para o desenvolvimento de IA de borda em dispositivos Windows. Isso inclui suporte especializado para hardware acelerado por NPU, integração com Windows ML e técnicas de otimização específicas para a plataforma.

**Guia Abrangente**: [Guia de Desenvolvimento de EdgeAI no Windows](../windowdeveloper.md)

Este guia cobre:
- Visão geral e componentes da plataforma Windows AI Foundry
- API Phi Silica para inferência eficiente em hardware NPU
- APIs de Visão Computacional para processamento de imagens e OCR
- Integração e otimização do runtime Windows ML
- CLI do Foundry Local para desenvolvimento e testes locais
- Estratégias de otimização de hardware para dispositivos Windows
- Exemplos práticos de implementação e melhores práticas

### Ferramenta de IA para Desenvolvimento de Edge AI
Para desenvolvedores que utilizam o Visual Studio Code, a extensão AI Toolkit oferece um ambiente de desenvolvimento abrangente, projetado especificamente para criar, testar e implementar aplicações de Edge AI. Esta ferramenta simplifica todo o fluxo de trabalho de desenvolvimento de Edge AI dentro do VS Code.

**Guia de Desenvolvimento**: [Ferramenta de IA para Desenvolvimento de Edge AI](../aitoolkit.md)

O guia da AI Toolkit cobre:
- Descoberta e seleção de modelos para implementação na borda
- Fluxos de trabalho de teste e otimização local
- Integração com ONNX e Ollama para modelos de borda
- Técnicas de conversão e quantização de modelos
- Desenvolvimento de agentes para cenários de borda
- Avaliação de desempenho e monitorização
- Preparação para implementação e melhores práticas

## Conclusão

Estas cinco implementações de EdgeAI demonstram a maturidade e a diversidade das soluções de IA de borda disponíveis atualmente. Desde dispositivos de borda acelerados por hardware, como o Jetson Orin Nano, até frameworks de software como ONNX Runtime GenAI e Windows ML, os desenvolvedores têm opções sem precedentes para implementar aplicações inteligentes na borda.

O fio condutor entre todas essas plataformas é a democratização das capacidades de IA, tornando o aprendizado de máquina sofisticado acessível a desenvolvedores de diferentes níveis de habilidade e casos de uso. Seja criando aplicações móveis, software para desktop ou sistemas embarcados, essas soluções de EdgeAI fornecem a base para a próxima geração de aplicações inteligentes que operam de forma eficiente e privada na borda.

Cada plataforma oferece vantagens únicas: Jetson Orin Nano para computação de borda acelerada por hardware, ONNX Runtime GenAI para desenvolvimento móvel multiplataforma, Azure EdgeAI para integração empresarial nuvem-borda, Windows ML para aplicações nativas do Windows e Foundry Local para implementações RAG focadas na privacidade. Juntas, elas representam um ecossistema abrangente para o desenvolvimento de EdgeAI.

---

