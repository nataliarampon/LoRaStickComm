class LoraCommands:

    ## Returns the firmware version and release date in format: "RN2903 X.Y.Z MMM DD YYYY HH:MM:SS"
    GET_VERSION = 'sys get ver'

    ## Sets the LoRA functionality to radio
    START_RADIO_OP = 'mac pause'

    ## Sets the radio pwr to the given value in dB (range from 2dB to 20dB)
    SET_RADIO_POWER = 'radio set pwr {}'

    ## Gets current operating mode (LoRa or FSK)
    GET_RADIO_MODE = 'radio get mod'

    ## Gets radio frequency
    GET_RADIO_FREQUENCY = 'radio get freq'

    ## Gets radio spreading factor (values can be sf7, sf8, sf9, sf10, sf11, sf12)
    GET_RADIO_SPREADING_FACTOR = 'radio get sf'

    ## Sets the radio functionality to receive continuously
    SET_CONTINUOUS_RADIO_RECEPTION = 'radio rx 0'

    ## Disables the watchdog timer timeout for continuous reception
    DISABLE_TIMEOUT = 'radio set wdt 0'

    ## Turns the LoRa stick LED on
    TURN_ON_LED = 'sys set pindig GPIO10 0'

    ## Turns the LoRa stick LED off
    TURN_OFF_LED = 'sys set pindig GPIO10 1'

    ## Data was successfully received
    RADIO_DATA_OK = 'ok'

    ## An error occured during radio operations
    RADIO_DATA_ERROR = 'radio_err'

    ## The radio line was busy
    RADIO_LINE_BUSY = 'busy'

    ## Input of radio command was invalid
    RADIO_INVALID_PARAM = 'invalid_param'

    ## Data received over radio
    RADIO_RADIO_DATA_RECEIVED = 'radio_rx'

    ## Radio data transmission was successful
    RADIO_TRANSFER_OK = 'radio_tx_ok'

    ## Radio transfer over radio
    RADIO_DATA_TRANSFER = 'radio tx {}'


