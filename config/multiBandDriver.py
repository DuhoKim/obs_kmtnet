# Load from sub-configurations
import os.path

for sub in ("mergeCoaddDetections", "measureCoaddSources", "mergeCoaddMeasurements", "forcedPhotCoadd"):
    path = os.path.join(os.path.dirname(__file__), sub + ".py")
    if os.path.exists(path):
        getattr(config, sub).load(path)
