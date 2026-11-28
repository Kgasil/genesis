# Marco 04 — Jornada de aprendizagem / Learning journey

28/11/2026. Marco 03 pausado por decisão do idealizador; 17/40 volumes complementares trabalhados (incluindo VII já registrada), 0/40 homologados. Notas, bloqueios e materiais preservados. Não se atribui aprovação acadêmica.

- Portal gratuito em `jornada.html`: 100 disciplinas (60 tecnologia, 40 negócios), 10 módulos tecnológicos, cinco trilhas empresariais, 15 projetos propostos e links públicos. Títulos tecnológicos recuperados do protocolo editorial histórico e faixas dos módulos do portal; títulos e horas empresariais extraídos da matriz pública. Horas individuais de tecnologia não presumidas. 4.000 + 2.000 = 6.000 horas nominais, 115 PDFs planejados e 5.280 páginas declaradas.
- Progresso autodeclarado por disciplina (não iniciado, teoria, prática, revisado), horas reais editáveis em incrementos de 15 min e projetos separados. Nenhum certificado ou equivalência. Sem duplicação automática de horas de projetos ou guias.
- Cronograma linear configurável (padrão 5 dias × 3h = 15h/semana; 400 semanas para 6.000h; 7 × 3h = 286 semanas). Não representa prazo garantido; não inclui pausas e não mede aprendizagem.
- Integração por propostas de portfólio e links para os cinco projetos GRAAL; nenhuma integração de software ou API presumida. Dados sintéticos, ambiente próprio/autorizado; nenhuma dependência externa para a jornada.
- Estado local em `genesis.journey.v1`, sem cadastro nem envio de progresso. Backup JSON validado por versão, IDs, tipos e limites, importação/reset com confirmação. Sem criptografia, sincronização ou garantia de disponibilidade; dados da mesma origem são acessíveis a scripts da mesma origem. Não inserir dados sensíveis.
- 27 verificações executadas sobre as funções puras e o catálogo no ambiente de preparação; suíte Node adicionada para reprodução. Navegador real, teste assistivo e implantação Pages ainda não verificados. Nenhum PDF ou ZIP de instalação alterado.
- Próximo: teste de uso real, recuperação privada dos arquivos tecnológicos ausentes conforme inventário histórico e validação de acessibilidade. Depois, piloto de aprendizagem com V01–V04 e projeto M01.

English: Milestone 03 paused, 17/40 worked on and zero approved. New free local-first journey with 100 subjects, adjustable schedule, 15 portfolio proposals and JSON backup. No academic certification, uploads, or live integrations. Browser, assistive technology and Pages deployment still need testing.

## Fase II — Diário e portfólio (28/11/2026)

- Migração v1→v2 preserva as horas históricas e etapas; v2 usa chave própria `genesis.journey.v2`. Saldo histórico somente leitura. Sessões concluídas têm intervalo em minutos (UTC), disciplina, tipo e nota curta; duração máxima 24h, sem sobreposição global. Não relançar horas do saldo histórico (não há datas para deduplicar retrospectivamente). Evidências têm disciplina, projeto, tipo, título, referência textual e revisão autodeclarada; não somam horas.
- Backup v2 JSON, importação também de v1, validação de schema, IDs, duração, duplicidades e sobreposição; substituição e exclusão confirmadas. Limites: 3.000 sessões, 1.000 evidências, 2 MB por importação. Conflitos de outra aba detectados antes de salvar, sem garantia transacional de gravação simultânea. Sem anexos nem dados sensíveis; estado local não criptografado. Fuso exibido conforme navegador; horário ambíguo em mudança de fuso/DST deve ser conferido pelo estudante.
- Percurso V01–V06: inventário fictício, algoritmo, Git, Python, Java, estruturas de dados e projeto M01 fila de chamados. Propostas GRAAL, não integração executável. Critérios: validação, ordenação, testes e README.
- 30 verificações diretas de funções puras nesta preparação, todas passaram. Workflow separado `journey-validation.yml` com Node e Chromium/Playwright; execução e resultado a conferir. Acessibilidade: rótulos, foco, regiões de status, navegação por teclado e reflow testáveis; leitor de tela e conformidade integral não presumidos. PDFs, biblioteca curricular, segurança do Mini e homologação suspensa preservados.

English: v2 local session ledger, read-only migrated historical balance, non-overlapping intervals, evidence registry with no extra hours, and V01–V06 practice path. No uploads, approvals or paid services. Browser CI and human accessibility evidence remain to be confirmed.

Correção de inspeção: mensagem de exclusão de sessão usava ID incorreto; corrigida e casos de exclusão adicionados ao teste Chromium. Backup com sessão futura recusado na importação. Verificação em CI pendente.

## Fase III — Metas e revisão espaçada (28/11/2026)

- Workflow 46148218729: build e deploy anteriores concluídos. Workflow 46148218730: Node e instalação Chromium aprovados; teste de reflow a 360 px falhou após os fluxos de migração, sessão, backup, exclusão e idioma. Correção responsiva sem ocultar overflow; CI nova preserva o teste e adiciona diagnóstico.
- Schema v3 na chave local existente, migração v1/v2; metas padrão de 900 minutos e cinco revisões por semana, editáveis. Semana segunda–domingo UTC; sessões repartidas no limite semanal; saldo histórico excluído da meta. Revisões autodeclaradas, uma por disciplina/dia UTC, não somam horas; intervalos heurísticos 1/3/7/14/30 dias, sem alegação de eficácia individual. Fila de até 20 itens e contagem integral. Backup inclui metas e revisões; versões antigas aceitas.
- V07–V11: cinco entregas M02 com SQLite, Python e painel HTML local, dados fictícios e reconciliação. Lilium é referência pedagógica, não integração instalada. 22 verificações diretas de lógica aprovadas; nova CI de navegador pendente de resultado. Página pública anterior implantada pelo Pages, consulta externa direta indisponível nesta execução. Nenhum PDF, ZIP do Mini ou bloqueio acadêmico alterado.

English: weekly UTC goals, spaced-review heuristic and M02 data path, with v1/v2 migration. The previous Pages deployment passed; Chromium exposed mobile overflow and the responsive fix is under regression testing. No academic approval or live Lilium integration.
