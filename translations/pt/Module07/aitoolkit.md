<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "65a22ed38b95f334dd8a893bf2c55806",
  "translation_date": "2025-10-02T12:28:13+00:00",
  "source_file": "Module07/aitoolkit.md",
  "language_code": "pt"
}
-->
# AI Toolkit para Visual Studio Code - Guia de Desenvolvimento de Edge AI

## Introdução

Bem-vindo ao guia completo para utilizar o AI Toolkit no Visual Studio Code no desenvolvimento de Edge AI. À medida que a inteligência artificial migra da computação centralizada na nuvem para dispositivos distribuídos na periferia, os programadores precisam de ferramentas poderosas e integradas que possam lidar com os desafios únicos do deployment na periferia - desde restrições de recursos até requisitos de operação offline.

O AI Toolkit para Visual Studio Code preenche esta lacuna ao oferecer um ambiente de desenvolvimento completo, especificamente projetado para criar, testar e otimizar aplicações de IA que funcionam eficientemente em dispositivos de periferia. Quer esteja a desenvolver para sensores IoT, dispositivos móveis, sistemas embutidos ou servidores de periferia, este toolkit simplifica todo o fluxo de trabalho de desenvolvimento dentro do ambiente familiar do VS Code.

Este guia irá conduzi-lo pelos conceitos essenciais, ferramentas e melhores práticas para aproveitar o AI Toolkit nos seus projetos de Edge AI, desde a seleção inicial de modelos até ao deployment em produção.

## Visão Geral

O AI Toolkit para Visual Studio Code é uma extensão poderosa que simplifica o desenvolvimento de agentes e a criação de aplicações de IA. O toolkit oferece capacidades abrangentes para explorar, avaliar e implementar modelos de IA de uma ampla gama de fornecedores—including Anthropic, OpenAI, GitHub, Google—enquanto suporta a execução local de modelos usando ONNX e Ollama.

O que diferencia o AI Toolkit é a sua abordagem abrangente ao ciclo de vida completo do desenvolvimento de IA. Ao contrário das ferramentas tradicionais de desenvolvimento de IA que se concentram em aspetos isolados, o AI Toolkit fornece um ambiente integrado que cobre descoberta de modelos, experimentação, desenvolvimento de agentes, avaliação e deployment—tudo dentro do ambiente familiar do VS Code.

A plataforma foi especificamente projetada para prototipagem rápida e deployment em produção, com funcionalidades como geração de prompts, iniciadores rápidos, integrações perfeitas com ferramentas MCP (Model Context Protocol) e capacidades extensivas de avaliação. Para o desenvolvimento de Edge AI, isto significa que pode desenvolver, testar e otimizar aplicações de IA para cenários de deployment na periferia de forma eficiente, mantendo o fluxo de trabalho completo de desenvolvimento dentro do VS Code.

## Objetivos de Aprendizagem

Ao final deste guia, será capaz de:

### Competências Principais
- **Instalar e configurar** o AI Toolkit para Visual Studio Code para fluxos de trabalho de desenvolvimento de Edge AI
- **Navegar e utilizar** a interface do AI Toolkit, incluindo o Catálogo de Modelos, Playground e Agent Builder
- **Selecionar e avaliar** modelos de IA adequados para deployment na periferia com base em desempenho e restrições de recursos
- **Converter e otimizar** modelos usando o formato ONNX e técnicas de quantização para dispositivos de periferia

### Competências de Desenvolvimento de Edge AI
- **Projetar e implementar** aplicações de Edge AI usando o ambiente de desenvolvimento integrado
- **Realizar testes de modelos** em condições semelhantes às da periferia usando inferência local e monitorização de recursos
- **Criar e personalizar** agentes de IA otimizados para cenários de deployment na periferia
- **Avaliar o desempenho de modelos** usando métricas relevantes para computação na periferia (latência, uso de memória, precisão)

### Otimização e Deployment
- **Aplicar técnicas de quantização e poda** para reduzir o tamanho do modelo mantendo um desempenho aceitável
- **Otimizar modelos** para plataformas de hardware específicas da periferia, incluindo aceleração por CPU, GPU e NPU
- **Implementar melhores práticas** para desenvolvimento de Edge AI, incluindo gestão de recursos e estratégias de fallback
- **Preparar modelos e aplicações** para deployment em dispositivos de periferia

### Conceitos Avançados de Edge AI
- **Integrar com frameworks de Edge AI** incluindo ONNX Runtime, Windows ML e TensorFlow Lite
- **Implementar arquiteturas multi-modelo** e cenários de aprendizagem federada para ambientes de periferia
- **Resolver problemas comuns de Edge AI** incluindo restrições de memória, velocidade de inferência e compatibilidade de hardware
- **Projetar estratégias de monitorização e registo** para aplicações de Edge AI em produção

### Aplicação Prática
- **Construir soluções completas de Edge AI** desde a seleção de modelos até ao deployment
- **Demonstrar proficiência** em fluxos de trabalho de desenvolvimento específicos para periferia e técnicas de otimização
- **Aplicar conceitos aprendidos** a casos de uso reais de Edge AI, incluindo IoT, dispositivos móveis e aplicações embutidas
- **Avaliar e comparar** diferentes estratégias de deployment de Edge AI e os seus trade-offs

## Funcionalidades Principais para Desenvolvimento de Edge AI

### 1. Catálogo de Modelos e Descoberta
- **Suporte Multi-Fornecedor**: Navegue e aceda a modelos de IA de Anthropic, OpenAI, GitHub, Google e outros fornecedores
- **Integração de Modelos Locais**: Descoberta simplificada de modelos ONNX e Ollama para deployment na periferia
- **Modelos do GitHub**: Integração direta com o alojamento de modelos do GitHub para acesso simplificado
- **Comparação de Modelos**: Compare modelos lado a lado para encontrar o equilíbrio ideal para as restrições de dispositivos de periferia

### 2. Playground Interativo
- **Ambiente de Teste Interativo**: Experimentação rápida com capacidades de modelos num ambiente controlado
- **Suporte Multi-modal**: Teste com imagens, texto e outros inputs típicos em cenários de periferia
- **Experimentação em Tempo Real**: Feedback imediato sobre respostas e desempenho do modelo
- **Otimização de Parâmetros**: Ajuste fino dos parâmetros do modelo para requisitos de deployment na periferia

### 3. Prompt (Agent) Builder
- **Geração de Linguagem Natural**: Gere prompts iniciais usando descrições em linguagem natural
- **Refinamento Iterativo**: Melhore os prompts com base nas respostas e desempenho do modelo
- **Decomposição de Tarefas**: Divida tarefas complexas com encadeamento de prompts e outputs estruturados
- **Suporte a Variáveis**: Utilize variáveis em prompts para comportamento dinâmico de agentes
- **Geração de Código de Produção**: Gere código pronto para produção para desenvolvimento rápido de aplicações

### 4. Execução em Massa e Avaliação
- **Teste Multi-Modelo**: Execute múltiplos prompts em modelos selecionados simultaneamente
- **Teste Eficiente em Escala**: Teste vários inputs e configurações de forma eficiente
- **Casos de Teste Personalizados**: Execute agentes com casos de teste para validar funcionalidades
- **Comparação de Desempenho**: Compare resultados entre diferentes modelos e configurações

### 5. Avaliação de Modelos com Conjuntos de Dados
- **Métricas Padrão**: Teste modelos de IA usando avaliadores integrados (F1 score, relevância, similaridade, coerência)
- **Avaliadores Personalizados**: Crie métricas de avaliação próprias para casos de uso específicos
- **Integração de Conjuntos de Dados**: Teste modelos contra conjuntos de dados abrangentes
- **Medição de Desempenho**: Quantifique o desempenho do modelo para decisões de deployment na periferia

### 6. Capacidades de Fine-tuning
- **Personalização de Modelos**: Personalize modelos para casos de uso e domínios específicos
- **Adaptação Especializada**: Adapte modelos a requisitos e domínios especializados
- **Otimização para Periferia**: Ajuste modelos especificamente para restrições de deployment na periferia
- **Treino Específico por Domínio**: Crie modelos adaptados a casos de uso específicos na periferia

### 7. Integração com Ferramentas MCP
- **Conectividade com Ferramentas Externas**: Conecte agentes a ferramentas externas através de servidores Model Context Protocol
- **Ações no Mundo Real**: Permita que agentes consultem bases de dados, acedam a APIs ou executem lógica personalizada
- **Servidores MCP Existentes**: Utilize ferramentas de comando (stdio) ou protocolos HTTP (eventos enviados pelo servidor)
- **Desenvolvimento Personalizado de MCP**: Construa e configure novos servidores MCP com testes no Agent Builder

### 8. Desenvolvimento e Teste de Agentes
- **Suporte a Chamadas de Função**: Permita que agentes invoquem funções externas dinamicamente
- **Teste de Integração em Tempo Real**: Teste integrações com execuções em tempo real e uso de ferramentas
- **Versionamento de Agentes**: Controle de versão para agentes com capacidades de comparação de resultados de avaliação
- **Depuração e Rastreamento**: Capacidades locais de rastreamento e depuração para desenvolvimento de agentes

## Fluxo de Trabalho de Desenvolvimento de Edge AI

### Fase 1: Descoberta e Seleção de Modelos
1. **Explore o Catálogo de Modelos**: Utilize o catálogo de modelos para encontrar modelos adequados para deployment na periferia
2. **Compare Desempenho**: Avalie modelos com base em tamanho, precisão e velocidade de inferência
3. **Teste Localmente**: Utilize modelos Ollama ou ONNX para testar localmente antes do deployment na periferia
4. **Avalie Requisitos de Recursos**: Determine as necessidades de memória e computação para dispositivos de periferia alvo

### Fase 2: Otimização de Modelos
1. **Converta para ONNX**: Converta modelos selecionados para o formato ONNX para compatibilidade com a periferia
2. **Aplique Quantização**: Reduza o tamanho do modelo através de quantização INT8 ou INT4
3. **Otimização de Hardware**: Otimize para hardware de periferia alvo (ARM, x86, aceleradores especializados)
4. **Validação de Desempenho**: Valide que os modelos otimizados mantêm uma precisão aceitável

### Fase 3: Desenvolvimento de Aplicações
1. **Design de Agentes**: Utilize o Agent Builder para criar agentes de IA otimizados para periferia
2. **Engenharia de Prompts**: Desenvolva prompts que funcionem eficazmente com modelos menores de periferia
3. **Teste de Integração**: Teste agentes em condições simuladas de periferia
4. **Geração de Código**: Gere código de produção otimizado para deployment na periferia

### Fase 4: Avaliação e Teste
1. **Avaliação em Massa**: Teste múltiplas configurações para encontrar as definições ideais para periferia
2. **Perfil de Desempenho**: Analise velocidade de inferência, uso de memória e precisão
3. **Simulação de Periferia**: Teste em condições semelhantes ao ambiente de deployment na periferia
4. **Teste de Stress**: Avalie o desempenho sob várias condições de carga

### Fase 5: Preparação para Deployment
1. **Otimização Final**: Aplique otimizações finais com base nos resultados dos testes
2. **Empacotamento para Deployment**: Empacote modelos e código para deployment na periferia
3. **Documentação**: Documente os requisitos e configurações de deployment
4. **Configuração de Monitorização**: Prepare monitorização e registo para deployment na periferia

## Público-Alvo para Desenvolvimento de Edge AI

### Programadores de Edge AI
- Programadores de aplicações que criam dispositivos de periferia e soluções IoT com IA
- Programadores de sistemas embutidos que integram capacidades de IA em dispositivos com restrições de recursos
- Programadores móveis que criam aplicações de IA em dispositivos como smartphones e tablets

### Engenheiros de Edge AI
- Engenheiros de IA que otimizam modelos para deployment na periferia e gerem pipelines de inferência
- Engenheiros DevOps que implementam e gerem modelos de IA em infraestruturas distribuídas de periferia
- Engenheiros de desempenho que otimizam cargas de trabalho de IA para restrições de hardware na periferia

### Investigadores e Educadores
- Investigadores de IA que desenvolvem modelos e algoritmos eficientes para computação na periferia
- Educadores que ensinam conceitos de Edge AI e demonstram técnicas de otimização
- Estudantes que aprendem sobre os desafios e soluções no deployment de Edge AI

## Casos de Uso de Edge AI

### Dispositivos IoT Inteligentes
- **Reconhecimento de Imagens em Tempo Real**: Implementar modelos de visão computacional em câmaras e sensores IoT
- **Processamento de Voz**: Implementar reconhecimento de fala e processamento de linguagem natural em altifalantes inteligentes
- **Manutenção Preditiva**: Executar modelos de deteção de anomalias em dispositivos industriais de periferia
- **Monitorização Ambiental**: Implementar modelos de análise de dados de sensores para aplicações ambientais

### Aplicações Móveis e Embutidas
- **Tradução no Dispositivo**: Implementar modelos de tradução de linguagem que funcionam offline
- **Realidade Aumentada**: Implementar reconhecimento e rastreamento de objetos em tempo real para aplicações de RA
- **Monitorização de Saúde**: Executar modelos de análise de saúde em dispositivos vestíveis e equipamentos médicos
- **Sistemas Autónomos**: Implementar modelos de tomada de decisão para drones, robôs e veículos

### Infraestrutura de Computação na Periferia
- **Data Centers de Periferia**: Implementar modelos de IA em data centers de periferia para aplicações de baixa latência
- **Integração com CDN**: Integrar capacidades de processamento de IA em redes de entrega de conteúdo
- **Periferia 5G**: Aproveitar a computação na periferia 5G para aplicações com IA
- **Computação em Névoa**: Implementar processamento de IA em ambientes de computação em névoa

## Instalação e Configuração

### Instalação da Extensão
Instale a extensão AI Toolkit diretamente do Visual Studio Code Marketplace:

**ID da Extensão**: `ms-windows-ai-studio.windows-ai-studio`

**Métodos de Instalação**:
1. **Marketplace do VS Code**: Pesquise por "AI Toolkit" na vista de Extensões
2. **Linha de Comando**: `code --install-extension ms-windows-ai-studio.windows-ai-studio`
3. **Instalação Direta**: Faça o download em [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

### Pré-requisitos para Desenvolvimento de Edge AI
- **Visual Studio Code**: Versão mais recente recomendada
- **Ambiente Python**: Python 3.8+ com bibliotecas de IA necessárias
- **ONNX Runtime** (Opcional): Para inferência de modelos ONNX
- **Ollama** (Opcional): Para servir modelos localmente
- **Ferramentas de Aceleração de Hardware**: CUDA, OpenVINO ou aceleradores específicos da plataforma

### Configuração Inicial
1. **Ativação da Extensão**: Abra o VS Code e verifique se o AI Toolkit aparece na Barra de Atividades
2. **Configuração de Fornecedores de Modelos**: Configure acesso ao GitHub, OpenAI, Anthropic ou outros fornecedores de modelos
3. **Ambiente Local**: Configure o ambiente Python e instale os pacotes necessários
4. **Aceleração de Hardware**: Configure aceleração por GPU/NPU, se disponível
5. **Integração MCP**: Configure servidores Model Context Protocol, se necessário

### Lista de Verificação para Configuração Inicial
- [ ] Extensão AI Toolkit instalada e ativada
- [ ] Catálogo de modelos acessível e modelos descobertos
- [ ] Playground funcional para teste de modelos
- [ ] Agent Builder acessível para desenvolvimento de prompts
- [ ] Ambiente de desenvolvimento local configurado
- [ ] Aceleração de hardware (se disponível) configurada corretamente

## Primeiros Passos com o AI Toolkit

### Guia de Início Rápido

Recomendamos começar com modelos alojados no GitHub para uma experiência mais simplificada:

1. **Instalação**: Siga o [guia de instalação](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup) para configurar o AI Toolkit no seu dispositivo
2. **Descoberta de Modelos**: Na vista de extensão, selecione **CATALOG > Models** para explorar os modelos disponíveis
3. **Modelos do GitHub**: Comece com modelos alojados no GitHub para integração otimizada
4. **Teste no Playground**: A partir de qualquer cartão de modelo, selecione **Try in Playground** para começar a experimentar as capacidades do modelo

### Desenvolvimento de Edge AI Passo a Passo

#### Passo 1: Exploração e Seleção de Modelos
1. Abra a vista do AI Toolkit na Barra de Atividades do VS Code
2. Navegue pelo Catálogo de Modelos para encontrar modelos adequados para deployment na periferia
3. Filtre por fornecedor (GitHub, ONNX, Ollama) com base nos seus requisitos de periferia
4. Utilize **Try in Playground** para testar imediatamente as capacidades do modelo

#### Passo 2: Desenvolvimento de Agentes
1. Utilize o **Prompt (Agent) Builder** para criar agentes de IA otimizados para periferia
2. Gerar prompts iniciais usando descrições em linguagem natural  
3. Iterar e refinar prompts com base nas respostas do modelo  
4. Integrar ferramentas MCP para capacidades avançadas dos agentes  

#### Passo 3: Teste e Avaliação  
1. Utilize **Bulk Run** para testar múltiplos prompts em modelos selecionados  
2. Execute agentes com casos de teste para validar a funcionalidade  
3. Avalie a precisão e o desempenho usando métricas integradas ou personalizadas  
4. Compare diferentes modelos e configurações  

#### Passo 4: Ajuste e Otimização  
1. Personalize modelos para casos de uso específicos  
2. Aplique ajustes específicos ao domínio  
3. Otimize para restrições de implementação em dispositivos de borda  
4. Versione e compare diferentes configurações de agentes  

#### Passo 5: Preparação para Implementação  
1. Gere código pronto para produção usando o Agent Builder  
2. Configure conexões com o servidor MCP para uso em produção  
3. Prepare pacotes de implementação para dispositivos de borda  
4. Configure métricas de monitorização e avaliação  

## Melhores Práticas para Desenvolvimento de IA na Borda  

### Seleção de Modelos  
- **Restrições de Tamanho**: Escolha modelos que se ajustem às limitações de memória dos dispositivos alvo  
- **Velocidade de Inferência**: Priorize modelos com tempos de inferência rápidos para aplicações em tempo real  
- **Compromissos de Precisão**: Equilibre a precisão do modelo com as restrições de recursos  
- **Compatibilidade de Formato**: Prefira formatos ONNX ou otimizados para hardware para implementação na borda  

### Técnicas de Otimização  
- **Quantização**: Utilize quantização INT8 ou INT4 para reduzir o tamanho do modelo e melhorar a velocidade  
- **Pruning**: Remova parâmetros desnecessários do modelo para reduzir os requisitos computacionais  
- **Distilação de Conhecimento**: Crie modelos menores que mantenham o desempenho de modelos maiores  
- **Aceleração de Hardware**: Aproveite NPUs, GPUs ou aceleradores especializados quando disponíveis  

### Fluxo de Trabalho de Desenvolvimento  
- **Testes Iterativos**: Teste frequentemente em condições semelhantes às da borda durante o desenvolvimento  
- **Monitorização de Desempenho**: Monitore continuamente o uso de recursos e a velocidade de inferência  
- **Controlo de Versões**: Acompanhe as versões dos modelos e as configurações de otimização  
- **Documentação**: Documente todas as decisões de otimização e os compromissos de desempenho  

### Considerações para Implementação  
- **Monitorização de Recursos**: Monitore memória, CPU e consumo de energia em produção  
- **Estratégias de Contingência**: Implemente mecanismos de fallback para falhas de modelo  
- **Mecanismos de Atualização**: Planeie atualizações de modelos e gestão de versões  
- **Segurança**: Implemente medidas de segurança adequadas para aplicações de IA na borda  

## Integração com Frameworks de IA na Borda  

### ONNX Runtime  
- **Implementação Multiplataforma**: Implemente modelos ONNX em diferentes plataformas de borda  
- **Otimização de Hardware**: Aproveite as otimizações específicas de hardware do ONNX Runtime  
- **Suporte Móvel**: Utilize ONNX Runtime Mobile para aplicações em smartphones e tablets  
- **Integração com IoT**: Implemente em dispositivos IoT usando distribuições leves do ONNX Runtime  

### Windows ML  
- **Dispositivos Windows**: Otimize para dispositivos de borda baseados em Windows e PCs  
- **Aceleração NPU**: Aproveite as Unidades de Processamento Neural em dispositivos Windows  
- **DirectML**: Utilize DirectML para aceleração GPU em plataformas Windows  
- **Integração UWP**: Integre com aplicações da Universal Windows Platform  

### TensorFlow Lite  
- **Otimização Móvel**: Implemente modelos TensorFlow Lite em dispositivos móveis e incorporados  
- **Delegados de Hardware**: Utilize delegados de hardware especializados para aceleração  
- **Microcontroladores**: Implemente em microcontroladores usando TensorFlow Lite Micro  
- **Suporte Multiplataforma**: Implemente em Android, iOS e sistemas Linux incorporados  

### Azure IoT Edge  
- **Híbrido Nuvem-Borda**: Combine treino na nuvem com inferência na borda  
- **Implementação de Módulos**: Implemente modelos de IA como módulos IoT Edge  
- **Gestão de Dispositivos**: Gerencie dispositivos de borda e atualizações de modelos remotamente  
- **Telemetria**: Colete dados de desempenho e métricas de modelos em implementações na borda  

## Cenários Avançados de IA na Borda  

### Implementação Multimodelo  
- **Conjuntos de Modelos**: Implemente múltiplos modelos para melhorar a precisão ou redundância  
- **Testes A/B**: Teste diferentes modelos simultaneamente em dispositivos de borda  
- **Seleção Dinâmica**: Escolha modelos com base nas condições atuais do dispositivo  
- **Partilha de Recursos**: Otimize o uso de recursos entre múltiplos modelos implementados  

### Aprendizagem Federada  
- **Treino Distribuído**: Treine modelos em múltiplos dispositivos de borda  
- **Preservação de Privacidade**: Mantenha os dados de treino local enquanto partilha melhorias de modelos  
- **Aprendizagem Colaborativa**: Permita que os dispositivos aprendam com experiências coletivas  
- **Coordenação Borda-Nuvem**: Coordene o treino entre dispositivos de borda e infraestrutura na nuvem  

### Processamento em Tempo Real  
- **Processamento de Fluxos**: Processe fluxos contínuos de dados em dispositivos de borda  
- **Inferência de Baixa Latência**: Otimize para latência mínima de inferência  
- **Processamento em Lote**: Processe lotes de dados de forma eficiente em dispositivos de borda  
- **Processamento Adaptativo**: Ajuste o processamento com base nas capacidades atuais do dispositivo  

## Resolução de Problemas no Desenvolvimento de IA na Borda  

### Problemas Comuns  
- **Restrições de Memória**: Modelo muito grande para a memória do dispositivo alvo  
- **Velocidade de Inferência**: Inferência do modelo muito lenta para requisitos em tempo real  
- **Degradação de Precisão**: A otimização reduz a precisão do modelo de forma inaceitável  
- **Compatibilidade de Hardware**: Modelo incompatível com o hardware alvo  

### Estratégias de Depuração  
- **Perfil de Desempenho**: Utilize as funcionalidades de rastreamento do AI Toolkit para identificar gargalos  
- **Monitorização de Recursos**: Monitore o uso de memória e CPU durante o desenvolvimento  
- **Testes Incrementais**: Teste otimizações de forma incremental para isolar problemas  
- **Simulação de Hardware**: Utilize ferramentas de desenvolvimento para simular o hardware alvo  

### Soluções de Otimização  
- **Quantização Adicional**: Aplique técnicas de quantização mais agressivas  
- **Arquitetura de Modelo**: Considere diferentes arquiteturas de modelo otimizadas para borda  
- **Otimização de Pré-processamento**: Otimize o pré-processamento de dados para restrições da borda  
- **Otimização de Inferência**: Utilize otimizações de inferência específicas para hardware  

## Recursos e Próximos Passos  

### Documentação Oficial  
- [Documentação para Desenvolvedores do AI Toolkit](https://aka.ms/AIToolkit/doc)  
- [Guia de Instalação e Configuração](https://code.visualstudio.com/docs/intelligentapps/overview#_install-and-setup)  
- [Documentação de Aplicações Inteligentes do VS Code](https://code.visualstudio.com/docs/intelligentapps)  
- [Documentação do Model Context Protocol (MCP)](https://modelcontextprotocol.io/)  

### Comunidade e Suporte  
- [Repositório GitHub do AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit)  
- [Problemas e Solicitações de Funcionalidades no GitHub](https://aka.ms/AIToolkit/feedback)  
- [Comunidade Discord do Azure AI Foundry](https://aka.ms/azureaifoundry/discord)  
- [Marketplace de Extensões do VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)  

### Recursos Técnicos  
- [Documentação do ONNX Runtime](https://onnxruntime.ai/)  
- [Documentação do Ollama](https://ollama.ai/)  
- [Documentação do Windows ML](https://docs.microsoft.com/en-us/windows/ai/)  
- [Documentação do Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/)  

### Caminhos de Aprendizagem  
- [Curso de Fundamentos de IA na Borda](../Module01/README.md)  
- [Guia de Modelos de Linguagem Pequenos](../Module02/README.md)  
- [Estratégias de Implementação na Borda](../Module03/README.md)  
- [Desenvolvimento de IA na Borda com Windows](./windowdeveloper.md)  

### Recursos Adicionais  
- **Estatísticas do Repositório**: Mais de 1.8k estrelas, 150+ forks, 18+ contribuidores  
- **Licença**: Licença MIT  
- **Segurança**: Aplicam-se as políticas de segurança da Microsoft  
- **Telemetria**: Respeita as configurações de telemetria do VS Code  

## Conclusão  

O AI Toolkit para Visual Studio Code representa uma plataforma abrangente para o desenvolvimento moderno de IA, oferecendo capacidades simplificadas para o desenvolvimento de agentes que são particularmente valiosas para aplicações de IA na borda. Com um extenso catálogo de modelos que suporta fornecedores como Anthropic, OpenAI, GitHub e Google, combinado com execução local através de ONNX e Ollama, o toolkit oferece a flexibilidade necessária para diversos cenários de implementação na borda.

A força do toolkit reside na sua abordagem integrada—desde a descoberta e experimentação de modelos no Playground até ao desenvolvimento sofisticado de agentes com o Prompt Builder, capacidades abrangentes de avaliação e integração perfeita com ferramentas MCP. Para desenvolvedores de IA na borda, isso significa prototipagem rápida e teste de agentes de IA antes da implementação na borda, com a capacidade de iterar rapidamente e otimizar para ambientes com restrições de recursos.

Vantagens principais para o desenvolvimento de IA na borda incluem:  
- **Experimentação Rápida**: Teste modelos e agentes rapidamente antes de comprometer-se com a implementação na borda  
- **Flexibilidade Multifornecedor**: Acesse modelos de várias fontes para encontrar soluções ideais para a borda  
- **Desenvolvimento Local**: Teste com ONNX e Ollama para desenvolvimento offline e preservação de privacidade  
- **Pronto para Produção**: Gere código pronto para produção e integre com ferramentas externas via MCP  
- **Avaliação Abrangente**: Utilize métricas integradas e personalizadas para validar o desempenho de IA na borda  

À medida que a IA continua a avançar para cenários de implementação na borda, o AI Toolkit para VS Code fornece o ambiente de desenvolvimento e o fluxo de trabalho necessários para construir, testar e otimizar aplicações inteligentes para ambientes com restrições de recursos. Quer esteja a desenvolver soluções IoT, aplicações de IA móvel ou sistemas de inteligência incorporada, o conjunto abrangente de funcionalidades e o fluxo de trabalho integrado do toolkit suportam todo o ciclo de vida do desenvolvimento de IA na borda.

Com desenvolvimento contínuo e uma comunidade ativa (mais de 1.8k estrelas no GitHub), o AI Toolkit permanece na vanguarda das ferramentas de desenvolvimento de IA, evoluindo continuamente para atender às necessidades dos desenvolvedores modernos de IA que constroem para cenários de implementação na borda.

[Next Foundry Local](./foundrylocal.md)  

---

**Aviso**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, é importante notar que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.