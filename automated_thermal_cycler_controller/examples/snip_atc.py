import time
import sys
import yaml

from pathlib import Path

from automated_thermal_cycler_controller import Client as ATCClient
from automated_thermal_cycler_controller.generated.automatedthermalcyclercontroller.automatedthermalcyclercontroller_errors import NotInitialized, InstrumentErrorOccurred, InvalidInstrumentStatusError, ProtocolNotLoaded, ProtocolNotValidated, InvalidProtocol

with open("config.yml", 'r') as file:
    config = yaml.safe_load(file)

host, port, cert = config["ATC"]["host"], config["ATC"]["port"], config["ATC"]["cert_path"]
print(f"Connect to ATC Server. host: {host} port: {port} cert file: {cert}")
atc_client = ATCClient(host, port, root_certs=Path(cert).read_bytes())

#region Load command
print("Load command start!")
with open(config["ATC"]["protocol_file_path"], 'rb') as file:
    load_instance = atc_client.AutomatedThermalCyclerController.Load(file.read())
while not load_instance.done:
    time.sleep(1)
    print("Load command is still running...")
print("Load command complete!")

try:
    load_instance.get_responses()
    print("Load succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except InvalidProtocol:
    print("Invalid protocol.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region Validate command
print("Validate command start!")
validate_instance = atc_client.AutomatedThermalCyclerController.Validate(0)
while not validate_instance.done:
    time.sleep(1)
    print("Validate command is still running...")
print("Validate command complete!")

try:
    validate_instance.get_responses()
    print("Validate succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except ProtocolNotLoaded:
    print("Any protocol is not loaded.")
    sys.exception()
except InvalidProtocol:
    print("Invalid protocol.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region OpenLid command
print("OpenLid command start!")
open_lid_instance = atc_client.AutomatedThermalCyclerController.OpenLid()
while not open_lid_instance.done:
    time.sleep(1)
    print("OpenLid command is still running...")
print("OpenLid command complete!")

try:
    open_lid_instance.get_responses()
    print("OpenLid succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region CloseLid command
print("CloseLid command start!")
close_lid_instance = atc_client.AutomatedThermalCyclerController.CloseLid()
while not close_lid_instance.done:
    time.sleep(1)
    print("CloseLid command is still running...")
print("CloseLid command complete!")

try:
    close_lid_instance.get_responses()
    print("CloseLid succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region StartRun command
print("StartRun command start!")
start_run_instance = atc_client.AutomatedThermalCyclerController.StartRun()
while not start_run_instance.done:
    time.sleep(1)
    print("StartRun command is still running...")
print("StartRun command complete!")

try:
    start_run_instance.get_responses()
    print("StartRun succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except ProtocolNotLoaded:
    print("Any protocol is not loaded.")
    sys.exception()
except InvalidProtocol:
    print("Invalid protocol.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region StopRun command
print("StopRun command start!")
stop_run_instance = atc_client.AutomatedThermalCyclerController.StopRun()
while not stop_run_instance.done:
    time.sleep(1)
    print("StopRun command is still running...")
print("StopRun command complete!")

try:
    stop_run_instance.get_responses()
    print("StopRun succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region GetInstrumentState command
print("GetInstrumentState command start!")
try:
    get_instrument_state_response = atc_client.AutomatedThermalCyclerController.GetInstrumentState()
    print("GetInstrumentState command complete!")
    print(f"GetInstrumentState succeeded. Status: {get_instrument_state_response.InstrumentState}")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion


#region Reset command
print("Reset command start!")
reset_instance = atc_client.AutomatedThermalCyclerController.Reset()
while not reset_instance.done:
    time.sleep(1)
    print("Reset command is still running...")
print("Reset command complete!")

try:
    reset_instance.get_responses()
    print("Reset succeeded.")
except NotInitialized:
    print("ATC is not initialized.")
    sys.exit()
except InstrumentErrorOccurred:
    print("Instrument Error occurred.")
    sys.exit()
except InvalidInstrumentStatusError:
    print("Invalid status.")
    sys.exit()
except:
    print("Undefined error occurred.")
    sys.exit()
#endregion

#region ElapsedTime property
print("Subscribe ElapsedTime property start.")
print(f"Current elapsed time: {atc_client.AutomatedThermalCyclerController.ElapsedTime.get()}")
elapsed_time_subscription = atc_client.AutomatedThermalCyclerController.ElapsedTime.subscribe()

print("New elapsed time:")
elapsed_time_subscription.add_callback(print)

time.sleep(5)

elapsed_time_subscription.cancel()
print("Subscribe ElapsedTime property complete.")
#endregion

#region RemainingTime property
print("Subscribe RemainingTime property start.")
# Wait briefly to avoid reading unexpected value.
# Immediately after starting the protocol, the RunTimeEvent has not occurred yet, so RemainingTime is still "00:00:00".
time.sleep(3)
print(f"Current remaining time: {atc_client.AutomatedThermalCyclerController.RemainingTime.get()}")
remaining_time_subscription = atc_client.AutomatedThermalCyclerController.RemainingTime.subscribe()

print("New remaining time:")
remaining_time_subscription.add_callback(print)
try:
    for remaining_time in remaining_time_subscription:
        if remaining_time == "00:00:00":
            break
finally:
    remaining_time_subscription.clear_callbacks()
    remaining_time_subscription.cancel

# Since it may take time to complete the running protocol, wait a bit just in case.
time.sleep(3)
print("Subscribe RemainingTime property complete.")
#endregion

#region Status property
print("Subscribe Status property start.")
print(f"Current status: {atc_client.AutomatedThermalCyclerController.Status.get()}")
status_subscription = atc_client.AutomatedThermalCyclerController.Status.subscribe()

print("New status:")
status_subscription.add_callback(print)

time.sleep(5)

status_subscription.cancel()
print("Subscribe Status property complete.")
#endregion