# Segurança / Security
<!-- kg-safe-distribution-v1 -->

## Distribuição segura / Secure distribution

- Não desative o Microsoft Defender, SmartScreen, Safe Browsing ou controles administrativos. Não restaure arquivos em quarentena para instalar. / Never disable security protections or restore quarantined files to install.
- Se houver alerta, interrompa a instalação. Registre o nome exato da detecção, versão, nome do arquivo, SHA-256 (se disponível) e produto de segurança. Informe pelo GitHub Issues sem incluir informações pessoais. / Stop installation on a warning and report the exact detection, version, filename, available SHA-256 and security product; omit personal data.
- Antes de uma nova publicação: revisar código e dependências, construir em ambiente limpo, conferir conteúdo do pacote e a correspondência com o código-fonte, publicar SHA-256 e notas de versão, verificar o pacote final com proteção atualizada em Windows e realizar instalação em máquina limpa. / Before release: review code and dependencies, build cleanly, verify package contents and source correspondence, publish SHA-256 and release notes, scan the final package on updated Windows and test installation on a clean machine.
- Extensões: privilegiar permissões mínimas e distribuição pelas lojas oficiais após revisão; instalação manual apenas para avaliação autorizada. Aplicativos Windows: utilizar assinatura Authenticode confiável quando disponível. A assinatura e o hash não são certificações de ausência de malware. / Prefer minimum permissions and official stores for extensions, and trusted Authenticode signing for Windows installers when available. Signing and hashes are not malware-free certifications.
- Uma detecção deve ser investigada, corrigida se procedente ou submetida à [Microsoft Security Intelligence](https://www.microsoft.com/en-us/wdsi/filesubmission) como possível falso positivo. Não alterar arquivos somente para escapar de detecção. / Investigate and remediate real detections or submit suspected false positives to Microsoft; do not change files solely to evade detection.
- Nenhuma versão deve ser anunciada como aprovada por antivírus sem evidência vinculada ao hash do pacote final, data, produto, versão das definições e resultado. / Never advertise antivirus approval without evidence tied to the exact final artifact hash, date, product, definition version and result.

> [!WARNING]
> **AVISO IMPORTANTE DE SEGURANÇA — Genesis Mini 0.1.0 (26/11/2026)**
>
> O Microsoft Defender detectou o pacote ZIP 0.1.0 como Trojan:Script/Ulthar.A!ml (ThreatID 2147751841), com alerta grave, e removeu o arquivo. Estamos investigando a causa e preparando a solicitação de análise oficial à Microsoft. Não há confirmação de falso positivo ou liberação. Nunca recomendamos desativar o Windows Defender, ignorar alertas ou restaurar arquivos em quarentena. A instalação permanece suspensa; o laboratório web está disponível sem instalação.
>
> Microsoft Defender detected the 0.1.0 ZIP as Trojan:Script/Ulthar.A!ml (ThreatID 2147751841), rated severe, and removed the file. We are investigating the cause and preparing an official review request to Microsoft. No false-positive determination or clearance has been confirmed. We never recommend disabling Windows Defender, bypassing warnings or restoring quarantined files. Installation remains paused; the web lab is available without installation.
>
> [Incidente oficial](https://github.com/Kgasil/genesis/issues/1) · [Mini Lab web](https://kgasil.github.io/genesis/mini/)
