# GRAAL Security & Trust 1.1 — Etapa 02 / Genesis Mini
Data: 2026-11-26. Escopo: análise estática e integridade do pacote original; sem alteração de interface, funcionalidades ou versão.

## Evidência do arquivo original
- Snapshot: `4c255490569cfadee6839d316f14dd7e67de7909` (branch backup-graal-security-trust-1.1-2026-11-26).
- Pacote: `downloads/Genesis-Mini-v0.1.0-install.zip`; 10.651 bytes; Git blob `323c674cf71a0336f519e37446f5f1806e3a7f17`.
- SHA-256 recalculado dos bytes recuperados via GitHub: `654d46b77439a4c196bd6c70bda0fc664f1f59e8a6fe745cad76e10ed7fc67b4`. Main e backup coincidem.
- Cinco entradas únicas, sem compressão, criptografia, arquivos executáveis nativos, caminhos inesperados, comentários, bytes extras ou dados fora das estruturas examinadas. CRC-32, cabeçalhos locais e centrais e correspondência com os cinco arquivos-fonte: PASS.

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| manifest.json | 246 | 655f62266c178debfa7d4431c6d1cda1a21830c6c5f4a6e52e9234cd2779e6e5 |
| popup.html | 2328 | 9443c813915a71b60b639c33a242f75ec4507daaad9285b75ae51d4226280e15 |
| style.css | 1785 | 75174dac08a206ded6e9bb2dd9afc943de2f320613f8a3f9225e837c2239bc8c |
| core.js | 2128 | 770ac3f9f61be71fd096357a6bad3a78acd7e7d4afa73ce9dae463a823b8ee3b |
| ui.js | 3674 | d99a6a43087d120d80f9b6525710848988e4deb7c9bb4acb945f0aab7d7183cd |

## Revisão estática
- Manifest V3: somente action/popup; nenhuma permission, host permission, background, content script ou native messaging declarada.
- HTML/CSS: referências locais, sem recursos remotos observados. Dois scripts locais, sem dependência npm de runtime declarada ou incorporada ao ZIP.
- core.js: regras locais, limite de 20.000 caracteres e validação numérica; sem execução dinâmica de texto, rede ou acesso ao sistema de arquivos.
- ui.js: entradas e resultados tratados como texto (textContent/createTextNode); cópia explícita via navigator.clipboard.writeText, sem leitura automática da área de transferência; sem transmissão externa ou persistência observada.
- Nenhum comportamento malicioso evidente encontrado nos cinco arquivos. Revisão estática não demonstra ausência absoluta de vulnerabilidades ou malware.
- Testes existentes: 19/19 PASS em Node v22.16.0 em Linux. Cópias do core.js e mini.test.js conferidas contra os Git blobs do backup antes de executar. Sintaxe core.js PASS. Interface instalada no navegador e comportamento no Windows não testados nesta etapa.

## Investigação do alerta
- Relato do titular: alerta na instalação. Nenhuma issue registrada no repositório na consulta; nome exato da detecção, arquivo afetado, histórico de proteção, produto de segurança e versão das definições ainda não fornecidos.
- Não é possível concluir se foi Defender Antivirus, SmartScreen ou alerta de instalação manual do navegador. Não classificar como falso positivo sem confirmação.
- Próximo passo: registrar os dados do alerta e comparar hash do arquivo detectado com o original, sem restaurar quarentena; análise em Windows com proteção atualizada na etapa 09. Possível falso positivo: https://www.microsoft.com/en-us/wdsi/filesubmission (envio sujeito a confirmação e resultado).
- Download direto continua suspenso. Não republicar, reempacotar ou alterar bytes para tentar evitar detecções. Mini Lab web continua disponível.
- Verificador de integridade: `python tests/verify_mini_package.py`. O verificador não substitui antivírus e deve falhar se o pacote histórico mudar.

## Estado
Auditoria estática e integridade: concluídas. Causa do alerta: pendente. Novo scan Defender: não realizado. Aprovação de instalação/distribuição: não concedida. Sem custo, sem alteração do pacote original.
