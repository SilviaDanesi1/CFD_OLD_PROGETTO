Density_Ref = 1.16431
Energy_Ref = 121830
HeatFlux_Ref = 163321*303.15
Pressure_Ref = 141848
Temperature_Ref = 303.15
Turb_Kin_Energy_Ref = 121830
Velocity_X_Ref = 349.042

# trace generated using paraview version 5.13.0
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
flowvtu = FindSource('flow.vtu')

# create a new 'Reflect'
reflect1 = Reflect(registrationName='Reflect1', Input=flowvtu)

# Properties modified on reflect1
reflect1.Plane = 'Y Max'

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
reflect1Display.Representation = 'Surface'

# hide data in view
Hide(flowvtu, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# rename source object
RenameSource('WholeBody', reflect1)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Density'))

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Density'
densityLUT = GetColorTransferFunction('Density')

# get opacity transfer function/opacity map for 'Density'
densityPWF = GetOpacityTransferFunction('Density')

# get 2D transfer function for 'Density'
densityTF2D = GetTransferFunction2D('Density')

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('Density', calculator1)

# Properties modified on calculator1
calculator1.ResultArrayName = 'Density_dim'
calculator1.Function = 'Density*1.16431'

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Density_dim'
density_dimLUT = GetColorTransferFunction('Density_dim')

# get opacity transfer function/opacity map for 'Density_dim'
density_dimPWF = GetOpacityTransferFunction('Density_dim')

# get 2D transfer function for 'Density_dim'
density_dimTF2D = GetTransferFunction2D('Density_dim')

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]

# get the material library
materialLibrary1 = GetMaterialLibrary()

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Energy'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(densityLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Energy'
energyLUT = GetColorTransferFunction('Energy')

# get opacity transfer function/opacity map for 'Energy'
energyPWF = GetOpacityTransferFunction('Energy')

# get 2D transfer function for 'Energy'
energyTF2D = GetTransferFunction2D('Energy')

# create a new 'Calculator'
calculator1_1 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('Energy', calculator1_1)

# Properties modified on calculator1_1
calculator1_1.ResultArrayName = 'Energy_dim'
calculator1_1.Function = 'Energy*121830'

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_1Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Energy_dim'
energy_dimLUT = GetColorTransferFunction('Energy_dim')

# get opacity transfer function/opacity map for 'Energy_dim'
energy_dimPWF = GetOpacityTransferFunction('Energy_dim')

# get 2D transfer function for 'Energy_dim'
energy_dimTF2D = GetTransferFunction2D('Energy_dim')

# hide data in view
Hide(calculator1_1, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Heat_Flux'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(energyLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Heat_Flux'
heat_FluxLUT = GetColorTransferFunction('Heat_Flux')

# get opacity transfer function/opacity map for 'Heat_Flux'
heat_FluxPWF = GetOpacityTransferFunction('Heat_Flux')

# get 2D transfer function for 'Heat_Flux'
heat_FluxTF2D = GetTransferFunction2D('Heat_Flux')

# create a new 'Calculator'
calculator1_2 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('HeatFlux', calculator1_2)

# Properties modified on calculator1_2
calculator1_2.ResultArrayName = 'HeatFlux_dim'
calculator1_2.Function = 'Heat_Flux*163321*303.15'

# show data in view
calculator1_2Display = Show(calculator1_2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_2Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'HeatFlux_dim'
heatFlux_dimLUT = GetColorTransferFunction('HeatFlux_dim')

# Rescale transfer function
heatFlux_dimLUT.RescaleTransferFunction(-1222334629165.7197, 5791044883.452445)

# get opacity transfer function/opacity map for 'HeatFlux_dim'
heatFlux_dimPWF = GetOpacityTransferFunction('HeatFlux_dim')

# Rescale transfer function
heatFlux_dimPWF.RescaleTransferFunction(-1222334629165.7197, 5791044883.452445)

# get 2D transfer function for 'HeatFlux_dim'
heatFlux_dimTF2D = GetTransferFunction2D('HeatFlux_dim')

# hide data in view
Hide(calculator1_2, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Pressure'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(heat_FluxLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Pressure'
pressureLUT = GetColorTransferFunction('Pressure')

# get opacity transfer function/opacity map for 'Pressure'
pressurePWF = GetOpacityTransferFunction('Pressure')

# get 2D transfer function for 'Pressure'
pressureTF2D = GetTransferFunction2D('Pressure')

# create a new 'Calculator'
calculator1_3 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('Pressure', calculator1_3)

# Properties modified on calculator1_3
calculator1_3.ResultArrayName = 'Pressure_dim'
calculator1_3.Function = 'Pressure*141848'

# show data in view
calculator1_3Display = Show(calculator1_3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_3Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Pressure_dim'
pressure_dimLUT = GetColorTransferFunction('Pressure_dim')

# get opacity transfer function/opacity map for 'Pressure_dim'
pressure_dimPWF = GetOpacityTransferFunction('Pressure_dim')

# get 2D transfer function for 'Pressure_dim'
pressure_dimTF2D = GetTransferFunction2D('Pressure_dim')

# hide data in view
Hide(calculator1_3, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Temperature'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(pressureLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Temperature'
temperatureLUT = GetColorTransferFunction('Temperature')

# get opacity transfer function/opacity map for 'Temperature'
temperaturePWF = GetOpacityTransferFunction('Temperature')

# get 2D transfer function for 'Temperature'
temperatureTF2D = GetTransferFunction2D('Temperature')

# create a new 'Calculator'
calculator1_4 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('Temperature', calculator1_4)

# Properties modified on calculator1_4
calculator1_4.ResultArrayName = 'Temperature_dim'
calculator1_4.Function = 'Temperature*303.15'

# show data in view
calculator1_4Display = Show(calculator1_4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_4Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_4Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Temperature_dim'
temperature_dimLUT = GetColorTransferFunction('Temperature_dim')

# get opacity transfer function/opacity map for 'Temperature_dim'
temperature_dimPWF = GetOpacityTransferFunction('Temperature_dim')

# get 2D transfer function for 'Temperature_dim'
temperature_dimTF2D = GetTransferFunction2D('Temperature_dim')

# hide data in view
Hide(calculator1_4, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Turb_Kin_Energy'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(temperatureLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Turb_Kin_Energy'
turb_Kin_EnergyLUT = GetColorTransferFunction('Turb_Kin_Energy')

# get opacity transfer function/opacity map for 'Turb_Kin_Energy'
turb_Kin_EnergyPWF = GetOpacityTransferFunction('Turb_Kin_Energy')

# get 2D transfer function for 'Turb_Kin_Energy'
turb_Kin_EnergyTF2D = GetTransferFunction2D('Turb_Kin_Energy')

# create a new 'Calculator'
calculator1_5 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('TurbKinEn', calculator1_5)

# Properties modified on calculator1_5
calculator1_5.ResultArrayName = 'TurbKinEn_dim'
calculator1_5.Function = 'Turb_Kin_Energy*121830'

# show data in view
calculator1_5Display = Show(calculator1_5, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_5Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_5Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'TurbKinEn_dim'
turbKinEn_dimLUT = GetColorTransferFunction('TurbKinEn_dim')

# get opacity transfer function/opacity map for 'TurbKinEn_dim'
turbKinEn_dimPWF = GetOpacityTransferFunction('TurbKinEn_dim')

# get 2D transfer function for 'TurbKinEn_dim'
turbKinEn_dimTF2D = GetTransferFunction2D('TurbKinEn_dim')

# hide data in view
Hide(calculator1_5, renderView1)

# set active source
SetActiveSource(reflect1)

# show data in view
reflect1Display = Show(reflect1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Velocity', 'Magnitude'))

# Hide the scalar bar for this color map if no visible data is colored by it.
HideScalarBarIfNotNeeded(turb_Kin_EnergyLUT, renderView1)

# rescale color and/or opacity maps used to include current data range
reflect1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
reflect1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'Velocity'
velocityLUT = GetColorTransferFunction('Velocity')

# get opacity transfer function/opacity map for 'Velocity'
velocityPWF = GetOpacityTransferFunction('Velocity')

# get 2D transfer function for 'Velocity'
velocityTF2D = GetTransferFunction2D('Velocity')

# set scalar coloring
ColorBy(reflect1Display, ('POINTS', 'Velocity', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
reflect1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(velocityLUT, reflect1Display)

# create a new 'Calculator'
calculator1_6 = Calculator(registrationName='Calculator1', Input=reflect1)

# rename source object
RenameSource('Velocity', calculator1_6)

# Properties modified on calculator1_6
calculator1_6.ResultArrayName = 'Velocity_dim'
calculator1_6.Function = 'Velocity_X*349.042'

# show data in view
calculator1_6Display = Show(calculator1_6, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
calculator1_6Display.Representation = 'Surface'

# hide data in view
Hide(reflect1, renderView1)

# show color bar/color legend
calculator1_6Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Velocity_dim'
velocity_dimLUT = GetColorTransferFunction('Velocity_dim')

# get opacity transfer function/opacity map for 'Velocity_dim'
velocity_dimPWF = GetOpacityTransferFunction('Velocity_dim')

# get 2D transfer function for 'Velocity_dim'
velocity_dimTF2D = GetTransferFunction2D('Velocity_dim')

# hide data in view
Hide(calculator1_6, renderView1)

# set active source
SetActiveSource(calculator1)

# show data in view
calculator1Display = Show(calculator1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 0.07000000029802322, 0.0, 0.014000000432133675, 0.0, 0.0, True, 0.9)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
density_dimLUT.ApplyPreset('Fast', True)

# get color legend/bar for density_dimLUT in view renderView1
density_dimLUTColorBar = GetScalarBar(density_dimLUT, renderView1)

# Properties modified on density_dimLUTColorBar
density_dimLUTColorBar.AutoOrient = 0
density_dimLUTColorBar.Orientation = 'Horizontal'
density_dimLUTColorBar.WindowLocation = 'Lower Center'
density_dimLUTColorBar.TitleFontSize = 15
density_dimLUTColorBar.LabelFontSize = 12
density_dimLUTColorBar.ScalarBarThickness = 15

# Properties modified on density_dimLUTColorBar
density_dimLUTColorBar.ScalarBarLength = 0.7

# Properties modified on density_dimLUTColorBar
density_dimLUTColorBar.ScalarBarLength = 0.5

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1698, 582)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134

# save screenshot
SaveScreenshot(filename='/Users/ilariaaltamura/Desktop/Density.png', viewOrLayout=renderView1, location=16, ImageResolution=[1920, 1080],
    TransparentBackground=1)

# hide data in view
Hide(calculator1, renderView1)

# set active source
SetActiveSource(calculator1_1)

# show data in view
calculator1_1Display = Show(calculator1_1, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_1Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
energy_dimLUT.ApplyPreset('Black-Body Radiation', True)

# get color legend/bar for energy_dimLUT in view renderView1
energy_dimLUTColorBar = GetScalarBar(energy_dimLUT, renderView1)

# Properties modified on energy_dimLUTColorBar
energy_dimLUTColorBar.AutoOrient = 0
energy_dimLUTColorBar.Orientation = 'Horizontal'
energy_dimLUTColorBar.WindowLocation = 'Lower Center'
energy_dimLUTColorBar.TitleFontSize = 15
energy_dimLUTColorBar.LabelFontSize = 12
energy_dimLUTColorBar.ScalarBarThickness = 15
energy_dimLUTColorBar.ScalarBarLength = 0.5

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 0.07000000029802322, 0.0, 0.014000000432133675, 0.0, 0.0, True, 0.9)

# layout/tab size in pixels
layout1.SetSize(1698, 582)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134

# save screenshot
SaveScreenshot(filename='/Users/ilariaaltamura/Desktop/Energy.png', viewOrLayout=renderView1, location=16, ImageResolution=[1920, 1080],
    TransparentBackground=1)

# hide data in view
Hide(calculator1_1, renderView1)

# set active source
SetActiveSource(calculator1_2)

# show data in view
calculator1_2Display = Show(calculator1_2, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_2Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# set active source
SetActiveSource(calculator1_3)

# show data in view
calculator1_3Display = Show(calculator1_3, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_3Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(calculator1_2, renderView1)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
pressure_dimLUT.ApplyPreset('Cool to Warm (Extended)', True)

# get color legend/bar for pressure_dimLUT in view renderView1
pressure_dimLUTColorBar = GetScalarBar(pressure_dimLUT, renderView1)

# Properties modified on pressure_dimLUTColorBar
pressure_dimLUTColorBar.AutoOrient = 0
pressure_dimLUTColorBar.Orientation = 'Horizontal'
pressure_dimLUTColorBar.WindowLocation = 'Lower Center'
pressure_dimLUTColorBar.TitleFontSize = 15
pressure_dimLUTColorBar.LabelFontSize = 12
pressure_dimLUTColorBar.ScalarBarThickness = 15
pressure_dimLUTColorBar.ScalarBarLength = 0.5

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 0.07000000029802322, 0.0, 0.014000000432133675, 0.0, 0.0, True, 0.9)

# layout/tab size in pixels
layout1.SetSize(1698, 582)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134

# save screenshot
SaveScreenshot(filename='/Users/ilariaaltamura/Desktop/Pressure.png', viewOrLayout=renderView1, location=16, ImageResolution=[1920, 1080],
    TransparentBackground=1)

# hide data in view
Hide(calculator1_3, renderView1)

# set active source
SetActiveSource(calculator1_4)

# show data in view
calculator1_4Display = Show(calculator1_4, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_4Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
temperature_dimLUT.ApplyPreset('Inferno (matplotlib)', True)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 0.07000000029802322, 0.0, 0.014000000432133675, 0.0, 0.0, True, 0.9)

# get color legend/bar for temperature_dimLUT in view renderView1
temperature_dimLUTColorBar = GetScalarBar(temperature_dimLUT, renderView1)

# Properties modified on temperature_dimLUTColorBar
temperature_dimLUTColorBar.AutoOrient = 0
temperature_dimLUTColorBar.Orientation = 'Horizontal'
temperature_dimLUTColorBar.WindowLocation = 'Lower Center'
temperature_dimLUTColorBar.TitleFontSize = 15
temperature_dimLUTColorBar.LabelFontSize = 12
temperature_dimLUTColorBar.ScalarBarThickness = 15
temperature_dimLUTColorBar.ScalarBarLength = 0.5

# layout/tab size in pixels
layout1.SetSize(1698, 582)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134

# save screenshot
SaveScreenshot(filename='/Users/ilariaaltamura/Desktop/Temperature.png', viewOrLayout=renderView1, location=16, ImageResolution=[1920, 1080],
    TransparentBackground=1)

# hide data in view
Hide(calculator1_4, renderView1)

# set active source
SetActiveSource(calculator1_6)

# show data in view
calculator1_6Display = Show(calculator1_6, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_6Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# hide data in view
Hide(calculator1_6, renderView1)

# show data in view
calculator1_6Display = Show(calculator1_6, renderView1, 'UnstructuredGridRepresentation')

# show color bar/color legend
calculator1_6Display.SetScalarBarVisibility(renderView1, True)

#changing interaction mode based on data extents
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.2345000009983778]

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# reset view to fit data bounds
renderView1.ResetCamera(0.0, 0.07000000029802322, 0.0, 0.014000000432133675, 0.0, 0.0, True, 0.9)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
velocity_dimLUT.ApplyPreset('Blue Orange (divergent)', True)

# get color legend/bar for velocity_dimLUT in view renderView1
velocity_dimLUTColorBar = GetScalarBar(velocity_dimLUT, renderView1)

# Properties modified on velocity_dimLUTColorBar
velocity_dimLUTColorBar.AutoOrient = 0
velocity_dimLUTColorBar.Orientation = 'Horizontal'
velocity_dimLUTColorBar.WindowLocation = 'Lower Center'
velocity_dimLUTColorBar.TitleFontSize = 15
velocity_dimLUTColorBar.LabelFontSize = 12
velocity_dimLUTColorBar.ScalarBarThickness = 15
velocity_dimLUTColorBar.ScalarBarLength = 0.5

# change representation type
calculator1_6Display.SetRepresentationType('Surface LIC')

# layout/tab size in pixels
layout1.SetSize(1698, 582)

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134

# save screenshot
SaveScreenshot(filename='/Users/ilariaaltamura/Desktop/Velocity.png', viewOrLayout=renderView1, location=16, ImageResolution=[1920, 1080],
    TransparentBackground=1)

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1698, 582)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.InteractionMode = '2D'
renderView1.CameraPosition = [0.03500000014901161, 0.007000000216066837, 0.137907690562351]
renderView1.CameraFocalPoint = [0.03500000014901161, 0.007000000216066837, 0.0]
renderView1.CameraParallelScale = 0.013313105592642134


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------