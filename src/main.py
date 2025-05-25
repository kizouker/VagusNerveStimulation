kjhifrom fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np

# Skapa en enklare visualisering att inkludera i LaTeX-projektplanen
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 8 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)
fft_result = np.abs(np.fft.fft(signal))[:250]

plt.figure()
plt.plot(fft_result)
plt.title("Exempel på FFT – Spektrum av sammansatt signal (8 Hz + 20 Hz)")
plt.xlabel("Frekvensindex")
plt.ylabel("Amplitud")
fft_img_path = "/mnt/data/fft_plot.png"
plt.tight_layout()
plt.savefig(fft_img_path)
plt.close()

# Skapa en LaTeX-projektplan
latex_content = r"""
\documentclass[12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{hyperref}
\usepackage{geometry}
\geometry{margin=2.5cm}

\title{Projektplan: Bioelektronisk signalanalys och HRV-styrd VNS-stimulering}
\author{Rickard Åberg}
\date{\today}

\begin{document}

\maketitle

\section*{Bakgrund}
Projektet syftar till att analysera och återskapa den typ av elektrisk stimulering som används i enheter som AlphaStim (CES - Cranial Electrotherapy Stimulation), med målet att skapa ett öppet, styrbart system där vagusnervstimulering anpassas efter individens HRV (Heart Rate Variability).

\section*{Översikt}
Målet är att:
\begin{itemize}
  \item Analysera AlphaStims utgångssignal med FFT.
  \item Modellera signalen med Heavisidefunktioner.
  \item Jämföra simulering med uppmätt signal (differensanalys).
  \item Skapa en styrbar signalgenerator (Arduino + DAC).
  \item Styra signalen dynamiskt med HRV och PID-reglering.
\end{itemize}

\section*{Fas 1: Signalinsamling och analys}
\begin{itemize}
  \item Sampla signal från AlphaStim via oscilloskop.
  \item Exportera till CSV eller binärt format.
  \item Utför FFT (Fast Fourier Transform) i Python.
  \item Identifiera grundfrekvenser och modulation.
\end{itemize}

\begin{figure}[h!]
\centering
\includegraphics[width=0.8\textwidth]{fft_plot.png}
\caption{Exempel på FFT av signal med 8 Hz och 20 Hz komponenter.}
\end{figure}

\section*{Fas 2: Signalgenerering}
\begin{itemize}
  \item Skapa Heavisidebaserade pulser i Arduino.
  \item Alternativt: generera sinus/trapetsform via DAC (t.ex. MCP4725).
  \item Design av lågpassfilter eller op-amp förstärkning.
\end{itemize}

\section*{Fas 3: Systemstyrning}
\begin{itemize}
  \item Läs HRV-data från Polar H10 / Elite HRV.
  \item Extrahera RMSSD, LF/HF etc. via Python.
  \item Designa en PID-regulator som styr VNS-signalens frekvens och amplitud.
\end{itemize}

\section*{Fas 4: Feedback och kalibrering}
\begin{itemize}
  \item Mäta den skapade signalen och jämföra med referens.
  \item Visa differens i frekvensdomän och tidsdomän.
  \item Iterera och förbättra reglerstrategin.
\end{itemize}

\section*{Verktyg och komponenter}
\begin{itemize}
  \item Python: NumPy, SciPy, Matplotlib, pyserial.
  \item Arduino Uno/Nano.
  \item MCP4725 DAC-modul.
  \item TL072 op-amp.
  \item USB-isolator och öronklämmor.
\end{itemize}

\section*{Vision}
Skapa en billig, öppen och adaptiv vagusnervstimulator som styrs av kroppens egna mönster och återkoppling – ett system för personlig återställning och balans, inspirerat av både teknik och fysiologi.

\end{document}
"""

# Spara LaTeX-filen
latex_path = "/mnt/data/projektplan_vns_hrv.tex"
with open(latex_path, "w") as f:
    f.write(latex_content)

latex_path, fft_img_path
