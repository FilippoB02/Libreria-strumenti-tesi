import pyvisa
import time

class GPP4323:
    """
    Libreria per controllare GW Instek GPP-4323 via SCPI tramite VISA.
    Compatibile con USB-TMC, USB-CDC (ASRL), RS232 e LAN (SOCKET).
    """

    def __init__(self, resource, timeout=2000):
        self.rm = pyvisa.ResourceManager()
        self.inst = self.rm.open_resource(resource)
        self.inst.timeout = timeout
        self.inst.read_termination = '\n'
        self.inst.write_termination = '\n'

    # ------------------------------------------------------------
    # Informazioni di base
    # ------------------------------------------------------------
    def idn(self):
        """Ritorna l'identificazione dello strumento."""
        return self.inst.query("*IDN?")

    def reset(self):
        """Reset dello strumento."""
        self.inst.write("*RST")

    def clear(self):
        """Reset degli status/errori."""
        self.inst.write("*CLS")

    # ------------------------------------------------------------
    # Selezione canale
    # ------------------------------------------------------------
    def select_channel(self, ch: int):
        """Seleziona il canale (1..4)."""
        self.inst.write(f"INST:NSEL {ch}")

    # ------------------------------------------------------------
    # Impostazioni di uscita
    # ------------------------------------------------------------
    def set_voltage(self, ch: int, volts: float):
        """Imposta la tensione di un canale."""
        self.inst.write(f"SOUR{ch}:VOLT {volts}")

    def set_current(self, ch: int, amps: float):
        """Imposta la corrente di un canale."""
        self.inst.write(f"SOUR{ch}:CURR {amps}")

    def output_on(self, ch: int):
        """Abilita l'uscita di un canale."""
        self.inst.write(f"OUTP{ch} ON")
        
    def output_on_wait(self, ch: int, delay=0.2):
        self.inst.write(f"OUTP{ch} ON")
        time.sleep(delay)

    def output_off(self, ch: int):
        """Disabilita l'uscita di un canale."""
        self.inst.write(f"OUTP{ch} OFF")

    # ------------------------------------------------------------
    # Lettura misure
    # ------------------------------------------------------------
    def measure_voltage(self, ch: int):
        """Legge la tensione del canale."""
        return float(self.inst.query(f"MEAS{ch}:VOLT?"))

    def measure_current(self, ch: int):
        """Legge la corrente del canale."""
        return float(self.inst.query(f"MEAS{ch}:CURR?"))

    # ------------------------------------------------------------
    # Funzioni varie
    # ------------------------------------------------------------
    def beep(self):
        """Esegue un beep (utile per debug)."""
        self.inst.write("BEEP")

    # ------------------------------------------------------------
    # Chiusura
    # ------------------------------------------------------------
    def close(self):
        """Chiude la connessione VISA."""
        self.inst.close()
        self.rm.close()