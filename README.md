# Acrobat Reader for Linux compatibility libraries for CentOS 7 and Fedora 32+

The Acrobat Reader for Linux (AcroRead) is one of the few PDF readers for Linux
that fully support XFA forms and therefore is still widely used, even though Adobe
stopped supporting it somewhere in 2013. 

On CentOS 5 and 6, the `AdobeReader_enu` package can be installed and
used without many problems. 

On CentOS 7 and Fedora 32+ however, life is not that easy.

## Problems with AcroRead on CentOS 7

First of all, some libraries are missing, most notably `libpangox-1.0.so.0`.
Unfortunately, even a rebuild of that package from the Fedora repositories does not 
make `acroread` usable.

Second, with the proper libraries built and installed, the `acroread` application
might start, but as soon as the user selects the **File** menu and chooses **Open** 
to open a file, `acroread` coredumps.

### Solution

In order to overcome these problems, I have put together a compatibility library RPM, 
based on 32bit libraries from CentOS 6. By installing this RPM, the missing requirements
when trying to install the `AcroRead_enu` RPM are fulfilled.
<br>
By repackaging the right libraries from CentOS 6, the coredumps are also
fixed and `acroread` becomes a usable application again.

### Installation

The missing libraries files are installed in the proper place for `acroread`
by installing
[AdobeReader-libs-1.0.0-1.el7.centos.i686.rpm](AdobeReader-libs-1.0.0-1.el7.centos.i686.rpm)

If you want get rid of the following annoying warning when starting `acroread`
```
  (acroread:9420): Gtk-WARNING **: Unable to locate theme engine in module_path: "clearlooks",
```
then make sure to also install the 32bit version of the 
[gtk2-engines-2.20.2-7.el7.i686.rpm](GTK2 engines)

In one go:

```
  yum install https://www.nikhef.nl/~janjust/acroread-libs/AdobeReader-libs-1.0.0-1.el7.centos.i686.rpm \
              https://www.nikhef.nl/~janjust/acroread-libs/gtk2-engines-2.20.2-7.el7.i686.rpm
```

**Note**: The distribution used in the version of the gtk2-engines rpm is '`el7`' instead of the 
CentOS 7 "default" of '`el7.centos`'.  This is done to avoid installation issues when installing both 
the 32bit and 64bit versions of the gtk2-engines package.


## Problems with AcroRead on Fedora 32+

As Acroread is getting older and older, compatibility with the libraries provided
by the OS is deteriorating. Starting with Fedora 33, it is no longer possible to 
install Acroread without having to (re)compile some compatibility libraries.

### Solution

In order to overcome these problems, I have put together a compatibility library RPM, 
based on the 32bit libraries from Fedora 32. By installing this RPM, the missing requirements
when trying to install the `AcroRead_enu` RPM are fulfilled.

Also, with this library there is no longer a need to install a large set of 32bit libraries,
as they are now included in this RPM. The downside is that if you have a **different**
32bit application that also relies on these libraries then you will need to install that one
first *before* installing this RPM do avoid any dependency issues.

## Installation

The missing libraries files are installed in the proper place for `acroread` by installing
[AdobeReader-libs-2.0.0-2.fc32.i686.rpm](AdobeReader-libs-2.0.0-2.fc32.i686.rpm)

If you want get rid of the following annoying warning when starting `acroread`
```
  (acroread:9420): Gtk-WARNING **: Unable to locate theme engine in module_path: "clearlooks",
```
then make sure to also install the 32bit version of the **GTK2 engines**, which unlike
CentOS 7, is still available for the (64bit) Fedora 32+.

In one go:
```
  dnf install https://www.nikhef.nl/~janjust/acroread-libs/AdobeReader-libs-2.0.0-2.fc32.i686.rpm \
              gtk2-engines.i686
```

This library has the following `provides`:
-
- `libGL.so.1`  
- `libGLU.so.1`
- `libcairo.so.2`
- `libgdk-x11-2.0.so.0`
- `libgtk-x11-2.0.so.0`
- `libharfbuzz.so.0`
- `libidn.so.11`
- `libpango-1.0.so.0`
- `libpangocairo-1.0.so.0`
- `libpangoft2-1.0.so.0`
- `libpangox-1.0.so.0`
- `libpangoxft-1.0.so.0`

but more libraries are included in the RPM, as the libraries above themselves depend on them.

