#/usr/bin/bash
echo ----------------------------------------------------------------
echo sIBL_GUI - Windows - Overall Build
echo ----------------------------------------------------------------

export PYINSTALLER=c:/pyinstaller
export APPLICATION=z:/Documents/Developement/sIBL_GUI
export PYTHONPATH=$APPLICATION/src

export SOURCE=$APPLICATION/src/siblgui
export RELEASES=$APPLICATION/releases/Windows
export DISTRIBUTION=$RELEASES/dist
export BUILD=$RELEASES/build
export DEPLOYMENT=$RELEASES/sIBL_GUI
export UTILITIES=$APPLICATION/utilities

#! Windows Build.
echo ----------------------------------------------------------------
echo Build - Begin
echo ----------------------------------------------------------------
rm -rf $BUILD $DISTRIBUTION
python $PYINSTALLER/Makespec.py --noconsole --icon "$SOURCE/resources/Icon_Light.ico" $SOURCE/sIBL_GUI.py -o $RELEASES
python $PYINSTALLER/Build.py $RELEASES/sIBL_GUI.spec
echo ----------------------------------------------------------------
echo Build - End
echo ----------------------------------------------------------------

#! Windows Release.
echo ----------------------------------------------------------------
echo Release - Begin
echo ----------------------------------------------------------------
rm -rf $DEPLOYMENT
cp -r $DISTRIBUTION/sIBL_GUI $RELEASES/
mkdir $DEPLOYMENT/ui
cp $SOURCE/ui/sIBL_GUI.ui $DEPLOYMENT/ui/
cp $SOURCE/ui/sIBL_GUI_Layouts.rc $DEPLOYMENT/ui/
cp $SOURCE/ui/Windows_styleSheet.qss $DEPLOYMENT/ui/
cp $SOURCE/ui/Darwin_styleSheet.qss $DEPLOYMENT/ui/
cp $SOURCE/ui/Linux_styleSheet.qss $DEPLOYMENT/ui/
mkdir $DEPLOYMENT/resources
cp $SOURCE/resources/Central_Widget.png $DEPLOYMENT/resources
cp $SOURCE/resources/Central_Widget_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Central_Widget_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Close_Cross.png $DEPLOYMENT/resources
cp $SOURCE/resources/Close_Cross_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Export.png $DEPLOYMENT/resources
cp $SOURCE/resources/Export_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Export_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Horizontal_Scrollbar_Grip.png $DEPLOYMENT/resources
cp $SOURCE/resources/Icon_Light.png $DEPLOYMENT/resources
cp $SOURCE/resources/Inspect.png $DEPLOYMENT/resources
cp $SOURCE/resources/Inspect_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Inspect_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Layout.png $DEPLOYMENT/resources
cp $SOURCE/resources/Layout_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Layout_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Library.png $DEPLOYMENT/resources
cp $SOURCE/resources/Library_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Library_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Miscellaneous.png $DEPLOYMENT/resources
cp $SOURCE/resources/Miscellaneous_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Miscellaneous_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Preferences.png $DEPLOYMENT/resources
cp $SOURCE/resources/Preferences_Active.png $DEPLOYMENT/resources
cp $SOURCE/resources/Preferences_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Resize_Grip.png $DEPLOYMENT/resources
cp $SOURCE/resources/sIBL_GUI_Logo.png $DEPLOYMENT/resources
cp $SOURCE/resources/sIBL_GUI_SpashScreen.png $DEPLOYMENT/resources
cp $SOURCE/resources/Small_Down_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/Small_Left_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/Small_Right_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/Small_Up_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/Thumbnail_Format_Not_Supported_Yet.png $DEPLOYMENT/resources
cp $SOURCE/resources/Thumbnail_Not_Found.png $DEPLOYMENT/resources
cp $SOURCE/resources/Tiny_Down_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/Tiny_Up_Arrow.png $DEPLOYMENT/resources
cp $SOURCE/resources/TreeView_Branch_Closed.png $DEPLOYMENT/resources
cp $SOURCE/resources/TreeView_Branch_End.png $DEPLOYMENT/resources
cp $SOURCE/resources/TreeView_Branch_More.png $DEPLOYMENT/resources
cp $SOURCE/resources/TreeView_Branch_Open.png $DEPLOYMENT/resources
cp $SOURCE/resources/TreeView_VLine.png $DEPLOYMENT/resources
cp $SOURCE/resources/Undock_Window.png $DEPLOYMENT/resources
cp $SOURCE/resources/Undock_Window_Hover.png $DEPLOYMENT/resources
cp $SOURCE/resources/Vertical_Scrollbar_Grip.png $DEPLOYMENT/resources
mkdir $DEPLOYMENT/templates
cp -r $SOURCE/templates/3dsMax/* $DEPLOYMENT/templates/
cp -r $SOURCE/templates/Maya/* $DEPLOYMENT/templates/
cp -r $SOURCE/templates/Softimage/* $DEPLOYMENT/templates/
cp -r $SOURCE/templates/XSI/* $DEPLOYMENT/templates/
cp -r $SOURCE/components $DEPLOYMENT
mkdir -p $DEPLOYMENT/libraries/freeImage/resources
cp $SOURCE/libraries/freeImage/resources/FreeImage.dll $DEPLOYMENT/libraries/freeImage/resources/
echo ----------------------------------------------------------------
echo Release - End
echo ----------------------------------------------------------------

#! Templates Textile Files Cleanup.
echo ----------------------------------------------------------------
echo Templates Textile Files Cleanup - Begin
echo ----------------------------------------------------------------
#! 3dsMax_MR_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/3dsMax_MR_Standard/help/3dsMax_MR_Standard Template Manual"

#! 3dsMax_Scanline_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/3dsMax_Scanline_Standard/help/3dsMax_Scanline_Standard Template Manual"

#! 3dsMax_VRay_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/3dsMax_VRay_Standard/help/3dsMax_VRay_Standard Template Manual"

#! Maya_Arnold_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_Arnold_Standard/help/Maya_Arnold_Standard Template Manual"

#! Maya_MR_Lightsmith Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_MR_Lightsmith/help/Maya_MR_Lightsmith Template Manual"

#! Maya_MR_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_MR_Standard/help/Maya_MR_Standard Template Manual"

#! Maya_RfM_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_RfM_Standard/help/Maya_RfM_Standard Template Manual"

#! Maya_VRay_Dome_Light Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_VRay_Dome_Light/help/Maya_VRay_Dome_Light Template Manual"

#! Maya_VRay_Lightsmith Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_VRay_Lightsmith/help/Maya_VRay_Lightsmith Template Manual"

#! Maya_VRay_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Maya_VRay_Standard/help/Maya_VRay_Standard Template Manual"

#! Softimage_Arnold_Dome_Light Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Softimage_Arnold_Dome_Light/help/Softimage_Arnold_Dome_Light Template Manual"

#! Softimage_Arnold_Lightsmith Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Softimage_Arnold_Lightsmith/help/Softimage_Arnold_Lightsmith Template Manual"

#! Softimage_Arnold_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Softimage_Arnold_Standard/help/Softimage_Arnold_Standard Template Manual"

#! Softimage_MR_Lightsmith Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Softimage_MR_Lightsmith/help/Softimage_MR_Lightsmith Template Manual"

#! Softimage_MR_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/Softimage_MR_Standard/help/Softimage_MR_Standard Template Manual"

#! XSI_Arnold_Dome_Light Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/XSI_Arnold_Dome_Light/help/XSI_Arnold_Dome_Light Template Manual"

#! XSI_Arnold_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/XSI_Arnold_Standard/help/XSI_Arnold_Standard Template Manual"

#! XSI_MR_Standard Textile Template Documentation Removal.
rm "$DEPLOYMENT/templates/XSI_MR_Standard/help/XSI_MR_Standard Template Manual"
echo ----------------------------------------------------------------
echo Templates Textile Files Cleanup - End
echo ----------------------------------------------------------------

#! Windows Release Cleanup.
echo ----------------------------------------------------------------
echo Cleanup - Begin
echo ----------------------------------------------------------------
python $UTILITIES/sIBL_GUI_recursiveRemove.py $DEPLOYMENT .pyc
python $UTILITIES/sIBL_GUI_recursiveRemove.py $DEPLOYMENT .pyo
python $UTILITIES/sIBL_GUI_recursiveRemove.py $DEPLOYMENT .DS_Store
python $UTILITIES/sIBL_GUI_recursiveRemove.py $DEPLOYMENT Thumbs.db
echo ----------------------------------------------------------------
echo Cleanup - End
echo ----------------------------------------------------------------