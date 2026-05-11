import pyvisa
import time

class GPP4323:
    """
    GW INSTEK GPP-4323 programmabre DC power supply
    
    High-level Python interface for controlling a GPP-4323 power supply
    using PyVISA library and SCPI commands.
    
    Need to download GPP driver setup from gwinstek website for USB connection

    Implements common SCPI commands for:
    - Identification
    - Reset / clear
    - Current and Voltage selection
    - Channel selection
    
    Examples
    --------
    >>> from fastruments.Keysight53220A import Keysight53220A
    >>> freq = Keysight53220A('USB0::0x0957::0x1807::MY63260252::INSTR')
    [53220A] IDN: Agilent Technologies,53220A,MY63260252,03.02-1924.2831-3.15-4.16-127-159-35
    [53220A] Connection successful.
    
    
    
    >>> freq.close()
    [53220A] Connection closed.
    
    FINISCI ESEMPIO
    
    """

    def __init__(self, resource, verbose: bool = True) -> None:
        """
        Initialize communication with GPP-4323 power supply.
        """
        
        self.resource = resource
        self.verbose = verbose
        self.connect()
        self.delay = 0.3
        
    # ---------------------------------------------------------
    # General communication and status
    # ---------------------------------------------------------
        
    def connect(self) -> None:
        """
        Establish the VISA connection and verify communication.
        """
        try:
            rm = pyvisa.ResourceManager()
            self.inst = rm.open_resource(self.resource)
            self.inst.read_termination = '\n'
            self.inst.write_termination = '\n'
        except Exception as e:
            raise ConnectionError(f"[GPP4323][ERROR] Failed to connect: {e}")

        try:
            self.idn()
            if self.verbose:
                print("[53220A] Connection successful.")
        except Exception as e:
            raise RuntimeError(f"[GPP4323][ERROR] IDN query failed: {e}")

    def idn(self) -> str:
        """
        Query the identification string.

        Returns
        -------
        str
            Full identification string.
        """
        idn = self.inst.query("*IDN?")
        if self.verbose:
            print(f"[GPP4323] IDN: {idn}")
        return idn

    def reset(self) -> None:
        """Reset the instrument to factory defaults."""
        self.inst.write("*RST")
        if self.verbose:
            print("[GPP4323] Instrument reset.")

    def clear(self) -> None:
        """Clear status and error registers."""
        self.inst.write("*CLS")
        if self.verbose:
            print("[GPP4323] Status registers cleared.")
        
    def close(self) -> None:
        """
        Close the VISA connection to the instrument.

        Notes
        -----
        Should always be called before program termination to release the USB resource.

        Raises
        ------
        RuntimeError
            If the resource cannot be cleanly closed.
        """
        try:
            self.inst.close()
            if self.verbose:
                print("[GPP4323] Connection closed.")
        except Exception as e:
            raise RuntimeError(f"[GPP4323][ERROR] Failed to close: {e}")
            
    """
    METTI APPOSTO I COMMENTI
    """

    # ------------------------------------------------------------
    # Output channel configuration
    # ------------------------------------------------------------
    
    def set_voltage(self, ch: int, volts: float):
        """Imposta la tensione di un canale."""
        self.inst.write(f"SOUR{ch}:VOLT {volts}")
        if self.verbose:
            print("[GPP4323] CH{ch}: Voltage set to {volts} V.")

    def set_current(self, ch: int, amps: float):
        """Imposta la corrente di un canale."""
        self.inst.write(f"SOUR{ch}:CURR {amps}")
        if self.verbose:
            print("[GPP4323] CH{ch}: current set to {amps} A.")
        
    """
    prova iset e vset e a cosa servono
    FAI LA FUNZIONE DI CHECK
    SCRIVI I COMMENTI
    
    funzione per la resistenza
    SOURce[1|2]:RESistor < NRf >
    serve usare mode CR ovvero resistenza costsnte, si comorta come carico
    """
        
    # ------------------------------------------------------------
    # Turning channels on and off
    # ------------------------------------------------------------

    def output_on(self, ch: int):
        """Abilita l'uscita di un canale."""
        self.inst.write(f"OUTP{ch} ON")
        time.sleep(self.delay)

    def output_off(self, ch: int):
        """Disabilita l'uscita di un canale."""
        self.inst.write(f"OUTP{ch} OFF")
        time.sleep(self.delay)
        
    def output_on_all(self):
        self.inst.write("ALLOUTON")
        time.sleep(self.delay)
        
    def output_off_all(self):
        self.inst.write("ALLOUTOFF")
        time.sleep(self.delay)
        
    """
    SCRIVI I COMMENTI E I VERBOSE
    """

    # ------------------------------------------------------------
    # Getting set parameters
    # ------------------------------------------------------------
    
    def measure_param(self, ch: int):
        volt = self.inst.query(f"MEAS{ch}:VOLT?")
        curr = self.inst.query(f"MEAS{ch}:CURR?")
        power = self.inst.query(f"MEAS{ch}:POWE?")
        if self.verbose:
            print(f"[GPP4323] CH{ch}: Measured values imposed by the instrument:")
            print(f"Voltage: {volt} V")
            print(f"Current: {curr} A")
            print(f"Power: {power} W")
        

    """
    devo fare anche quello che fa get del valore impostato
    o solo quello del valore effettivamnte erogato?
    SCRIVI I COMMENTI
    """
    
    # ------------------------------------------------------------
    # Setting series and parallel channel 1 - 2
    # ------------------------------------------------------------
    
    def series(self, state: str):
        self.inst.write(f"OUTP:SER {state}")
        time.sleep(self.delay)
        
    def parallel(self, state: str):
        self.inst.write(f"OUTP:PAR {state}")
        time.sleep(self.delay)
    
    """
    SCRIVI I COMMENTI
    """
    
    """
    SCRIVI IL MAIN
    """