# Detecção de Formas Geométricas

Projeto em Python usando OpenCV para detectar formas geométricas em vídeo/imagem com segmentação por cor (HSV). Inclui ferramentas de calibração dos limites HSV e um detector que marca e rotula as formas encontradas.

## Visão Geral
- `detector_formas.py`: lê o vídeo em `assets/video_desafio_1.mp4`, segmenta por cor com limites HSV por forma e desenha os contornos e rótulos.
- `calibrador_hsv.py`: calibra os limites HSV em tempo real sobre o vídeo (trackbars e pausa com espaço).
- `calibrador_img_hsv.py`: calibra os limites HSV sobre uma imagem estática (`assets/13_frame_000004_t6.00s.jpg`).

## Pré-requisitos
- Python 3.9+ (recomendado)
- Windows PowerShell (o projeto inclui instruções específicas para Windows)

## Instalação
No diretório do projeto:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
 .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Para desativar o ambiente virtual:

```powershell
deactivate
```

Se o PowerShell bloquear scripts, você pode usar somente nesta sessão:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## Estrutura
```
assets/
calibrador_hsv.py
calibrador_img_hsv.py
detector_formas.py
requirements.txt
README.md
```

## Uso

### 1) Calibrar HSV no Vídeo
Use quando quiser ajustar limites HSV diretamente no fluxo do vídeo.

```powershell
python calibrador_hsv.py
```
- Tecla espaço: pausa/retoma o vídeo.
- Ajuste `H Min/Max`, `S Min/Max`, `V Min/Max` até a máscara destacar somente a cor desejada.
- Anote os valores para preencher o `SHAPE_DATABASE` do `detector_formas.py`.

### 2) Calibrar HSV na Imagem
Use quando preferir calibrar a partir de um frame ou imagem estática.

```powershell
python calibrador_img_hsv.py
```
- Ajuste os trackbars e observe a máscara.
- Use os limites resultantes para atualizar o `SHAPE_DATABASE`.

### 3) Detectar Formas no Vídeo

```powershell
python detector_formas.py
```
- O script aplica blur, converte para HSV, segmenta pelas faixas de cada forma e desenha contornos e labels.
- Pressione `q` para sair.

## Configuração de Cores (SHAPE_DATABASE)
No `detector_formas.py`, ajuste os arrays `lower` e `upper` (HSV) para cada forma. Exemplo:

```python
"CIRCULO": {
	'color_label': "Azul",
	'lower': np.array([103, 102, 169]),
	'upper': np.array([112, 147, 255])
}
```

Se uma forma não tiver limites definidos, o detector a ignora.

## Dependências
- `opencv-python`
- `numpy`

Instaladas via `requirements.txt`.