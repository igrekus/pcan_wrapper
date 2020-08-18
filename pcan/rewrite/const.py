from ctypes import c_ushort, c_ubyte, c_char_p
from aenum import Enum

MAX_LENGTH_HARDWARE_NAME = 33  # Maximum device name length: 32 characters + terminator
MAX_LENGTH_VERSION_STRING = 18  # Maximum version string length: 17 characters + terminator


class PCANHandle(Enum):
    """
    Currently defined and supported PCAN interfaces and channels
    """
    _init_ = 'value __doc__'

    NONE = 0x00, 'Undefined/default value for a PCAN bus'

    ISA_1 = 0x21, 'ISA interface, channel 1'
    ISA_2 = 0x22, 'ISA interface, channel 2'
    ISA_3 = 0x23, 'ISA interface, channel 3'
    ISA_4 = 0x24, 'ISA interface, channel 4'
    ISA_5 = 0x25, 'ISA interface, channel 5'
    ISA_6 = 0x26, 'ISA interface, channel 6'
    ISA_7 = 0x27, 'ISA interface, channel 7'
    ISA_8 = 0x28, 'ISA interface, channel 8'

    DONGLE = 0x31, 'Dongle/LPT interface, channel 1'

    PCI_1 = 0x41, 'PCI interface, channel 1'
    PCI_2 = 0x42, 'PCI interface, channel 2'
    PCI_3 = 0x43, 'PCI interface, channel 3'
    PCI_4 = 0x44, 'PCI interface, channel 4'
    PCI_5 = 0x45, 'PCI interface, channel 5'
    PCI_6 = 0x46, 'PCI interface, channel 6'
    PCI_7 = 0x47, 'PCI interface, channel 7'
    PCI_8 = 0x48, 'PCI interface, channel 8'
    PCI_9 = 0x409, 'PCI interface, channel 9'
    PCI_11 = 0x40B, 'PCI interface, channel 11'
    PCI_12 = 0x40C, 'PCI interface, channel 12'
    PCI_13 = 0x40D, 'PCI interface, channel 13'
    PCI_10 = 0x40A, 'PCI interface, channel 10'
    PCI_14 = 0x40E, 'PCI interface, channel 14'
    PCI_15 = 0x40F, 'PCI interface, channel 15'
    PCI_16 = 0x410, 'PCI interface, channel 16'

    USB_1 = 0x51, 'USB interface, channel 1'
    USB_2 = 0x52, 'USB interface, channel 2'
    USB_3 = 0x53, 'USB interface, channel 3'
    USB_4 = 0x54, 'USB interface, channel 4'
    USB_5 = 0x55, 'USB interface, channel 5'
    USB_6 = 0x56, 'USB interface, channel 6'
    USB_7 = 0x57, 'USB interface, channel 7'
    USB_8 = 0x58, 'USB interface, channel 8'
    USB_9 = 0x509, 'USB interface, channel 9'
    USB_10 = 0x50A, 'USB interface, channel 10'
    USB_11 = 0x50B, 'USB interface, channel 11'
    USB_12 = 0x50C, 'USB interface, channel 12'
    USB_13 = 0x50D, 'USB interface, channel 13'
    USB_14 = 0x50E, 'USB interface, channel 14'
    USB_15 = 0x50F, 'USB interface, channel 15'
    USB_16 = 0x510, 'USB interface, channel 16'

    PCC_1 = 0x61, 'PC Card interface, channel 1'
    PCC_2 = 0x62, 'PC Card interface, channel 2'

    LAN_1 = 0x801, 'LAN interface, channel 1'
    LAN_2 = 0x802, 'LAN interface, channel 2'
    LAN_3 = 0x803, 'LAN interface, channel 3'
    LAN_4 = 0x804, 'LAN interface, channel 4'
    LAN_5 = 0x805, 'LAN interface, channel 5'
    LAN_6 = 0x806, 'LAN interface, channel 6'
    LAN_7 = 0x807, 'LAN interface, channel 7'
    LAN_8 = 0x808, 'LAN interface, channel 8'
    LAN_9 = 0x809, 'LAN interface, channel 9'
    LAN_10 = 0x80A, 'LAN interface, channel 10'
    LAN_11 = 0x80B, 'LAN interface, channel 11'
    LAN_12 = 0x80C, 'LAN interface, channel 12'
    LAN_13 = 0x80D, 'LAN interface, channel 13'
    LAN_14 = 0x80E, 'LAN interface, channel 14'
    LAN_15 = 0x80F, 'LAN interface, channel 15'
    LAN_16 = 0x810, 'LAN interface, channel 16'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ushort(self.value)


class PCANStatus(Enum):
    """
    PCAN error and status codes
    """
    _init_ = 'value __doc__'

    ERROR_OK = 0x00000, 'No error'
    ERROR_XMTFULL = 0x00001, 'Transmit buffer in CAN controller is full'
    ERROR_OVERRUN = 0x00002, 'CAN controller was read too late'
    ERROR_BUSLIGHT = 0x00004, 'Bus error: an error counter reached the "light" limit'
    ERROR_BUSHEAVY = 0x00008, 'Bus error: an error counter reached the "heavy" limit'
    ERROR_BUSWARNING = ERROR_BUSHEAVY[0], 'Bus error: an error counter reached the "warning" limit'
    ERROR_BUSPASSIVE = 0x40000, 'Bus error: the CAN controller is error passive'
    ERROR_BUSOFF = 0x00010, 'Bus error: the CAN controller is in bus-off state'
    ERROR_ANYBUSERR = ERROR_BUSWARNING[0] | ERROR_BUSLIGHT[0] | ERROR_BUSHEAVY[0] | ERROR_BUSOFF[0] | ERROR_BUSPASSIVE[
        0], 'Mask for all bus errors'
    ERROR_QRCVEMPTY = 0x00020, 'Receive queue is empty'
    ERROR_QOVERRUN = 0x00040, 'Receive queue was read too late'
    ERROR_QXMTFULL = 0x00080, 'Transmit queue is full'
    ERROR_REGTEST = 0x00100, 'Test of the CAN controller hardware registers failed (no hardware found)'
    ERROR_NODRIVER = 0x00200, 'Driver not loaded'
    ERROR_HWINUSE = 0x00400, 'Hardware already in use by a Net'
    ERROR_NETINUSE = 0x00800, 'A Client is already connected to the Net'
    ERROR_ILLHW = 0x01400, 'Hardware handle is invalid'
    ERROR_ILLNET = 0x01800, 'Net handle is invalid'
    ERROR_ILLCLIENT = 0x01C00, 'Client handle is invalid'
    ERROR_ILLHANDLE = ERROR_ILLHW[0] | ERROR_ILLNET[0] | ERROR_ILLCLIENT[0], 'Mask for all handle errors'
    ERROR_RESOURCE = 0x02000, 'Resource (FIFO, Client, timeout) cannot be created'
    ERROR_ILLPARAMTYPE = 0x04000, 'Invalid parameter'
    ERROR_ILLPARAMVAL = 0x08000, 'Invalid parameter value'
    ERROR_UNKNOWN = 0x10000, 'Unknown error'
    ERROR_ILLDATA = 0x20000, 'Invalid data, function, or action'
    ERROR_ILLMODE = 0x80000, 'Driver object state is wrong for the attempted operation'
    ERROR_CAUTION = 0x2000000, 'An operation was successfully carried out, however, irregularities were registered'
    ERROR_INITIALIZE = 0x4000000, 'Channel is not initialized [Value was changed from 0x40000 to 0x4000000]'
    ERROR_ILLOPERATION = 0x8000000, 'Invalid operation [Value was changed from 0x80000 to 0x8000000]'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'


class PCANDevice(Enum):
    """
    PCAN devices
    """
    _init_ = 'value __doc__'
    PCAN_NONE = 0x00, 'Undefined, unknown or not selected PCAN device value'
    PCAN_PEAKCAN = 0x01, 'PCAN Non-PnP devices. NOT USED WITHIN PCAN-Basic API'
    PCAN_ISA = 0x02, 'PCAN-ISA, PCAN-PC/104, and PCAN-PC/104-Plus'
    PCAN_DNG = 0x03, 'PCAN-Dongle'
    PCAN_PCI = 0x04, 'PCAN-PCI, PCAN-cPCI, PCAN-miniPCI, and PCAN-PCI Express'
    PCAN_USB = 0x05, 'PCAN-USB and PCAN-USB Pro'
    PCAN_PCC = 0x06, 'PCAN-PC Card'
    PCAN_VIRTUAL = 0x07, 'PCAN Virtual hardware. NOT USED WITHIN PCAN-Basic API'
    PCAN_LAN = 0x08, 'PCAN Gateway devices'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ubyte(self.value)


class PCANParams(Enum):
    """"
    PCAN parameters
    """
    _init_ = 'value __doc__'

    PCAN_DEVICE_ID = 0x01, 'Device identifier parameter'
    PCAN_5VOLTS_POWER = 0x02, '5-Volt power parameter'
    PCAN_RECEIVE_EVENT = 0x03, 'PCAN receive event handler parameter'
    PCAN_MESSAGE_FILTER = 0x04, 'PCAN message filter parameter'
    PCAN_API_VERSION = 0x05, 'PCAN-Basic API version parameter'
    PCAN_CHANNEL_VERSION = 0x06, 'PCAN device channel version parameter'
    PCAN_BUSOFF_AUTORESET = 0x07, 'PCAN Reset-On-Busoff parameter'
    PCAN_LISTEN_ONLY = 0x08, 'PCAN Listen-Only parameter'
    PCAN_LOG_LOCATION = 0x09, 'Directory path for log files'
    PCAN_LOG_STATUS = 0x0A, 'Debug-Log activation status'
    PCAN_LOG_CONFIGURE = 0x0B, 'Configuration of the debugged information (LOG_FUNCTION_***)'
    PCAN_LOG_TEXT = 0x0C, 'Custom insertion of text into the log file'
    PCAN_CHANNEL_CONDITION = 0x0D, 'Availability status of a PCAN-Channel'
    PCAN_HARDWARE_NAME = 0x0E, 'PCAN hardware name parameter'
    PCAN_RECEIVE_STATUS = 0x0F, 'Message reception status of a PCAN-Channel'
    PCAN_CONTROLLER_NUMBER = 0x10, 'CAN-Controller number of a PCAN-Channel'
    PCAN_TRACE_LOCATION = 0x11, 'Directory path for PCAN trace files'
    PCAN_TRACE_STATUS = 0x12, 'CAN tracing activation status'
    PCAN_TRACE_SIZE = 0x13, 'Configuration of the maximum file size of a CAN trace'
    PCAN_TRACE_CONFIGURE = 0x14, 'Configuration of the trace file storing mode (TRACE_FILE_***)'
    PCAN_CHANNEL_IDENTIFYING = 0x15, 'Physical identification of a USB based PCAN-Channel by blinking its associated LED'
    PCAN_CHANNEL_FEATURES = 0x16, 'Capabilities of a PCAN device (FEATURE_***)'
    PCAN_BITRATE_ADAPTING = 0x17, 'Using of an existing bit rate (PCAN-View connected to a channel)'
    PCAN_BITRATE_INFO = 0x18, 'Configured bit rate as Btr0Btr1 value'
    PCAN_BITRATE_INFO_FD = 0x19, 'Configured bit rate as TPCANBitrateFD string'
    PCAN_BUSSPEED_NOMINAL = 0x1A, 'Configured nominal CAN Bus speed as Bits per seconds'
    PCAN_BUSSPEED_DATA = 0x1B, 'Configured CAN data speed as Bits per seconds'
    PCAN_IP_ADDRESS = 0x1C, 'Remote address of a LAN channel as string in IPv4 format'
    PCAN_LAN_SERVICE_STATUS = 0x1D, 'Status of the Virtual PCAN-Gateway Service'
    PCAN_ALLOW_STATUS_FRAMES = 0x1E, 'Status messages reception status within a PCAN-Channel'
    PCAN_ALLOW_RTR_FRAMES = 0x1F, 'RTR messages reception status within a PCAN-Channel'
    PCAN_ALLOW_ERROR_FRAMES = 0x20, 'Error messages reception status within a PCAN-Channel'
    PCAN_INTERFRAME_DELAY = 0x21, 'Delay, in microseconds, between sending frames'
    PCAN_ACCEPTANCE_FILTER_11BIT = 0x22, 'Filter over code and mask patterns for 11-Bit messages'
    PCAN_ACCEPTANCE_FILTER_29BIT = 0x23, 'Filter over code and mask patterns for 29-Bit messages'
    PCAN_IO_DIGITAL_CONFIGURATION = 0x24, 'Output mode of 32 digital I/O pin of a PCAN-USB Chip. 1: Output-Active 0 : Output Inactive'
    PCAN_IO_DIGITAL_VALUE = 0x25, 'Value assigned to a 32 digital I/O pins of a PCAN-USB Chip'
    PCAN_IO_DIGITAL_SET = 0x26, 'Value assigned to a 32 digital I/O pins of a PCAN-USB Chip - Multiple digital I/O pins to 1 = High'
    PCAN_IO_DIGITAL_CLEAR = 0x27, 'Clear multiple digital I/O pins to 0'
    PCAN_IO_ANALOG_VALUE = 0x28, 'Get value of a single analog input pin'
    PCAN_FIRMWARE_VERSION = 0x29, 'Get the version of the firmware used by the device associated with a PCAN-Channel'
    PCAN_ATTACHED_CHANNELS_COUNT = 0x2A, 'Get the amount of PCAN channels attached to a system'
    PCAN_ATTACHED_CHANNELS = 0x2B, 'Get information about PCAN channels attached to a system'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ubyte(self.value)


class PCANParamValues(Enum):
    """"
    PCAN parameter values
    """
    _init_ = 'value __doc__'

    # TODO extract each group to it's own class

    PCAN_PARAMETER_OFF = 0x00, 'The PCAN parameter is not set (inactive)'
    PCAN_PARAMETER_ON = 0x01, 'The PCAN parameter is set (active)'
    PCAN_FILTER_CLOSE = 0x00, 'The PCAN filter is closed. No messages will be received'
    PCAN_FILTER_OPEN = 0x01, 'The PCAN filter is fully opened. All messages will be received'
    PCAN_FILTER_CUSTOM = 0x02, 'The PCAN filter is custom configured. Only registered messages will be received'
    PCAN_CHANNEL_UNAVAILABLE = 0x00, 'The PCAN-Channel handle is illegal, or its associated hardware is not available'
    PCAN_CHANNEL_AVAILABLE = 0x01, 'The PCAN-Channel handle is available to be connected (PnP Hardware: it means furthermore that the hardware is plugged-in)'
    PCAN_CHANNEL_OCCUPIED = 0x02, 'The PCAN-Channel handle is valid, and is already being used'
    PCAN_CHANNEL_PCANVIEW = PCAN_CHANNEL_AVAILABLE[0] | PCAN_CHANNEL_OCCUPIED[
        0], 'The PCAN-Channel handle is already being used by a PCAN-View application, but is available to connect'

    LOG_FUNCTION_DEFAULT = 0x00, 'Logs system exceptions / errors'
    LOG_FUNCTION_ENTRY = 0x01, 'Logs the entries to the PCAN-Basic API functions'
    LOG_FUNCTION_PARAMETERS = 0x02, 'Logs the parameters passed to the PCAN-Basic API functions'
    LOG_FUNCTION_LEAVE = 0x04, 'Logs the exits from the PCAN-Basic API functions'
    LOG_FUNCTION_WRITE = 0x08, 'Logs the CAN messages passed to the CAN_Write function'
    LOG_FUNCTION_READ = 0x10, 'Logs the CAN messages received within the CAN_Read function'
    LOG_FUNCTION_ALL = 0xFFFF, 'Logs all possible information within the PCAN-Basic API functions'

    TRACE_FILE_SINGLE = 0x00, '# A single file is written until it size reaches PAN_TRACE_SIZE'
    TRACE_FILE_SEGMENTED = 0x01, '# Traced data is distributed in several files with size PAN_TRACE_SIZE'
    TRACE_FILE_DATE = 0x02, '# Includes the date into the name of the trace file'
    TRACE_FILE_TIME = 0x04, '# Includes the start time into the name of the trace file'
    TRACE_FILE_OVERWRITE = 0x80, '# Causes the overwriting of available traces (same name)'

    FEATURE_FD_CAPABLE = 0x01, 'Device supports flexible data-rate (CAN-FD)'
    FEATURE_DELAY_CAPABLE = 0x02, 'Device supports a delay between sending frames (FPGA based USB devices)'
    FEATURE_IO_CAPABLE = 0x04, 'Device supports I/O functionality for electronic circuits (USB-Chip devices)'

    SERVICE_STATUS_STOPPED = 0x01, 'The service is not running'
    SERVICE_STATUS_RUNNING = 0x04, 'The service is running'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'


class PCANMessageType(Enum):
    """"
    PCAN message types
    """
    _init_ = 'value __doc__'

    PCAN_MESSAGE_STANDARD = 0x00, 'The PCAN message is a CAN Standard Frame (11-bit identifier)'
    PCAN_MESSAGE_RTR = 0x01, 'The PCAN message is a CAN Remote-Transfer-Request Frame'
    PCAN_MESSAGE_EXTENDED = 0x02, 'The PCAN message is a CAN Extended Frame (29-bit identifier)'
    PCAN_MESSAGE_FD = 0x04, 'The PCAN message represents a FD frame in terms of CiA Specs'
    PCAN_MESSAGE_BRS = 0x08, 'The PCAN message represents a FD bit rate switch (CAN data at a higher bit rate)'
    PCAN_MESSAGE_ESI = 0x10, 'The PCAN message represents a FD error state indicator(CAN FD transmitter was error active)'
    PCAN_MESSAGE_ERRFRAME = 0x40, 'The PCAN message represents an error frame'
    PCAN_MESSAGE_STATUS = 0x80, 'The PCAN message represents a PCAN status message'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ubyte(self.value)


class PCANBaudRate(Enum):
    """
    Represents a PCAN Baud rate register value

    Baud rate codes = BTR0/BTR1 register values for the CAN controller.
    You can define your own Baud rate with the BTROBTR1 register.
    Take a look at www.peak-system.com for our free software "BAUDTOOL"
    to calculate the BTROBTR1 register for every bit rate and sample point.
    """
    _init_ = 'value __doc__'

    PCAN_BAUD_1M = 0x0014, '1 MBit/s'
    PCAN_BAUD_800K = 0x0016, '800 kBit/s'
    PCAN_BAUD_500K = 0x001C, '500 kBit/s'
    PCAN_BAUD_250K = 0x011C, '250 kBit/s'
    PCAN_BAUD_125K = 0x031C, '125 kBit/s'
    PCAN_BAUD_100K = 0x432F, '100 kBit/s'
    PCAN_BAUD_95K = 0xC34E, '95,238 kBit/s'
    PCAN_BAUD_83K = 0x852B, '83,333 kBit/s'
    PCAN_BAUD_50K = 0x472F, '50 kBit/s'
    PCAN_BAUD_47K = 0x1414, '47,619 kBit/s'
    PCAN_BAUD_33K = 0x8B2F, '33,333 kBit/s'
    PCAN_BAUD_20K = 0x532F, '20 kBit/s'
    PCAN_BAUD_10K = 0x672F, '10 kBit/s'
    PCAN_BAUD_5K = 0x7F7F, '5 kBit/s'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ushort(self.value)


class PCANBitRate(Enum):
    """
    Represents a PCAN-FD bit rate string

    Represents the configuration for a CAN bit rate
    Note:
       * Each parameter and its value must be separated with a '='.
       * Each pair of parameter/value must be separated using ','.

    Example:
       f_clock=80000000,nom_brp=10,nom_tseg1=5,nom_tseg2=2,nom_sjw=1,data_brp=4,data_tseg1=7,data_tseg2=2,data_sjw=1
    """
    _init_ = 'value __doc__'

    # TODO add value docstrings
    PCAN_BR_CLOCK = "f_clock", ''
    PCAN_BR_CLOCK_MHZ = "f_clock_mhz", ''
    PCAN_BR_NOM_BRP = "nom_brp", ''
    PCAN_BR_NOM_TSEG1 = "nom_tseg1", ''
    PCAN_BR_NOM_TSEG2 = "nom_tseg2", ''
    PCAN_BR_NOM_SJW = "nom_sjw", ''
    PCAN_BR_NOM_SAMPLE = "nom_sam", ''
    PCAN_BR_DATA_BRP = "data_brp", ''
    PCAN_BR_DATA_TSEG1 = "data_tseg1", ''
    PCAN_BR_DATA_TSEG2 = "data_tseg2", ''
    PCAN_BR_DATA_SJW = "data_sjw", ''
    PCAN_BR_DATA_SAMPLE = "data_ssp_offset", ''

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: s={repr(self.value)} b={self.value.encode("ASCII")}>'

    @property
    def as_ctype(self):
        return c_char_p(self.value.encode('ASCII'))


class PCANNonPnpType(Enum):
    """
    Supported Non-PnP Hardware types
    """
    _init_ = 'value __doc__'

    PCAN_TYPE_ISA = 0x01, 'PCAN-ISA 82C200'
    PCAN_TYPE_ISA_SJA = 0x09, 'PCAN-ISA SJA1000'
    PCAN_TYPE_ISA_PHYTEC = 0x04, 'PHYTEC ISA'
    PCAN_TYPE_DNG = 0x02, 'PCAN-Dongle 82C200'
    PCAN_TYPE_DNG_EPP = 0x03, 'PCAN-Dongle EPP 82C200'
    PCAN_TYPE_DNG_SJA = 0x05, 'PCAN-Dongle SJA1000'
    PCAN_TYPE_DNG_SJA_EPP = 0x06, 'PCAN-Dongle EPP SJA1000'

    def __str__(self):
        return f'<{self.__class__.__name__}.{self.name}: d={self.value} h={self.value:X} b={self.value:b}>'

    @property
    def as_ctype(self):
        return c_ubyte(self.value)
