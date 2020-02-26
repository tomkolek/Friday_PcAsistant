Friday - Osobysty asystent
-------
*tylko dla Windows (testowane na Windows 10)*

---

**Friday** to osobisty asystent, który jest we wczesnej fazie rozwoju. Aby go wywołać Powiedz "Hej Friday"

#### Funkcje:
* gfds
* Cross-platform GUI (Qt)
* USB HID (no need to install any drivers)
* The device is simple to build (just Do-It-Yourself)

---

### Prismatik Build Instructions for Windows
#### Prerequisites:
* [Qt SDK](http://qt-project.org/downloads), you may need to set `%QTDIR%` (sysdm.cpl &rarr; Advanced &rarr; Environment Variables &rarr; New) to something like `C:\Qt\x.xx.x\msvc_xxxx\`.
* Visual Studio, [Windows SDK](https://msdn.microsoft.com/en-us/windows/desktop/ff851942.aspx) or [Microsoft DirectX SDK](http://www.microsoft.com/en-us/download/details.aspx?id=6812)
* optional (if you want to create an installer) POSIX shell utilities [MSYS for example](http://www.mingw.org/wiki/MSYS). 
* optional [any](https://wiki.openssl.org/index.php/Binaries) [OpenSSL binaries](https://slproweb.com/products/Win32OpenSSL.html) to include them in the setup. If you just want to build, you can skip them in `build-vars.prf` (this will render the update check ineffective).
* optional [BASS and BASSWASAPI](http://www.un4seen.com/) for the Sound Visualizer. You can skip them in `build-vars.prf`.

#### Build Process:
1. Go to `<repo>/Software`
2. Copy and edit `build-vars.prf` according to your machine
3. Optional: if locales changed: run `update_locales.bat` or `./update_locales.sh` (slow on Windows)
4. Run `scripts/win32/generate_sln.bat` (from the Visual Studio Developer prompt / `vcvarsall.bat`)
5. Build `Lightpack.sln` with MSBuild / VisualStudio

#### Building an Installer:
1. Run `scripts/win32/prepare_installer.sh`. (This builds the autoupdater (UpdateElevate), needs the submodule checked out and currently works only with VS2015).
2. Build `dist_windows/script.iss` (64bit) or `script32.iss` (32bit) with ISCC (the InnoSetup compiler)

---

### Build Instructions for Linux
#### Prerequisites:
You will need the following packages, usually all of them are in distro's repository:
* qt5-default
* libqt5serialport5-dev
* build-essential
* libgtk2.0-dev
* libusb-1.0-0-dev
* libnotify-dev
* libudev-dev
* qttools5-dev-tools
* if you are using Ubuntu: libappindicator-dev
* not required, but the update checker uses SSL sockets: openssl

#### Build Process:
1. Go to `<repo>/Software`
2. Optional: if locales changed: run `./update_locales.sh`
3. Run `qmake -r`
4. Run `make`


#### Building a deb Package:
1. Run `scripts/linux/prepare_installer.sh`
2. `cd dist_linux` and run `build-deb.sh`

#### Manual Deployment:
Instead of building a deb package, you can:

1. Add a rule for **UDEV**. See comments from `<repo>/Software/dist_linux/deb/etc/udev/rules.d/93-lightpack.rules` for how to do it.
2. Make sure `<repo>/Software/qtserialport/libQt5SerialPort.so.5` is available for loading by *Prismatik* (place it in appropriate dir or use *LD_LIBRARY_PATH* variable)

---

### Build Instructions for OS X
#### Prerequisites:
* Qt SDK (5.0+)
* MacOSX 10.9.sdk

###### Whole Dependencies List for Prismatik 5.10.1:
* QtCore.framework
* QtGui.framework
* QtNetwork.framework
* QtOpenGL.framework

#### Build Process:
1. Download and unpack 5.0+ **Qt SDK** from www.qt-project.org
2. Go to `<repo>/Software`
3. Optional: if locales changed: run `./update_locales.sh`
4. CLI
   1. Run `qmake -r`
   2. Run `make`
5. or Xcode
   1. Run `./scripts/macos/generate_xcode_project.sh`
   2. Open `Lightpack.xcodeproj`


#### Building a dmg package:
1. Run `macdeployqt bin/Prismatik.app -dmg`

---

### Firmware Build Instructions

**Updating Firmware on Windows:**
If you don't want to build the firmware yourself, you can follow the [documentation](https://github.com/Atarity/Lightpack-docs/blob/master/EN/Lightpack_firmware_update_with_FLIP_utility.md) for flashing the latest firmware on Windows.

*Please note that these instructions are for Debian based systems.*

**Compiling Firmware Only:**

1. Install [AVR GCC Toolchain](http://avr-eclipse.sourceforge.net/wiki/index.php/The_AVR_GCC_Toolchain): `sudo apt-get install gcc-avr binutils-avr avr-libc`
2. Compile the firmware:
  * `cd Firmware`
  * `make LIGHTPACK_HW=7` (or any other hardware version 4-7)
  * Alternatively, you can do `./build_batch.sh` to build the firmware for all hardware versions
3. The firmware can be found in the same directory (individual build) or *Firmware/hex* (batch build).

**Compiling and Uploading Firmware to Device:**

1. Install [AVR GCC Toolchain](http://avr-eclipse.sourceforge.net/wiki/index.php/The_AVR_GCC_Toolchain) and **dfu-programmer**: `sudo apt-get install gcc-avr binutils-avr avr-libc avrdude dfu-programmer`
2. Reboot device to bootloader (via the secret button on the device)
3. Compile and upload the firmware:
  * `cd Firmware`
  * `make LIGHTPACK_HW=7 && make dfu LIGHTPACK_HW=7` (or any other hardware version 4-7)

---

Please let us know if you find mistakes, bugs or errors. Contributions are welcome.<br />
Post new issue : https://github.com/psieg/Lightpack/issues
