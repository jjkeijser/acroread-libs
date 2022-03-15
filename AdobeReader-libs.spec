
%define debug_package %{nil}
#%define __arch_install_post %{nil}
#%define __os_install_post %{nil}
#%define __spec_install_post %{nil}

%define _build_id_links none

BuildArch:     i686
Name:          AdobeReader-libs
Version:       2.0.0
Release:       2%{?dist}
License:       Commercial 
Group:         Applications/Publishing
Summary:       Adobe Reader compatibility libraries for Fedora 32+
URL:           http://www.nikhef.nl/~janjust/acroread-libs

Source:        AdobeReader-libs-%{version}.tar.gz
AutoProv:      no
AutoReq:       no

# It provides the following libraries BUT in the wrong location!
Provides:      libGL.so.1
Provides:      libGLU.so.1
Provides:      libcairo.so.2
Provides:      libgdk-x11-2.0.so.0
Provides:      libgtk-x11-2.0.so.0
Provides:      libharfbuzz.so.0
Provides:      libidn.so.11
Provides:      libpango-1.0.so.0
Provides:      libpangocairo-1.0.so.0
Provides:      libpangoft2-1.0.so.0
Provides:      libpangox-1.0.so.0
Provides:      libpangoxft-1.0.so.0

# The following list is far from complete...
Requires:      libXau.so.6
Requires:      libXext.so.6
Requires:      libX11.so.6
Requires:      libXinerama.so.1
Requires:      libXrandr.so.2
Requires:      libXcomposite.so.1
Requires:      libXft.so.2

%description
Compatibility libraries to allow you to run AdobeReader on Fedora 32+
without having to install ALL 32bit libraries.

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT

# create dirs
mkdir -p $RPM_BUILD_ROOT/opt/Adobe/Reader9/Reader/intellinux/lib

# copy over the files from the tarballs
cp -a lib* $RPM_BUILD_ROOT/opt/Adobe/Reader9/Reader/intellinux/lib


%files
%defattr(-,root,root,-)
/opt/Adobe/Reader9/Reader/intellinux/lib/libGL.so.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libGL.so.1.7.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLU.so.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLU.so.1.3.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLX.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLX.so.0.0.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLdispatch.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLdispatch.so.0.0.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libcairo.so.2
/opt/Adobe/Reader9/Reader/intellinux/lib/libcairo.so.2.11600.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libdatrie.so.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libdatrie.so.1.3.2
/opt/Adobe/Reader9/Reader/intellinux/lib/libfribidi.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libfribidi.so.0.4.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libgdk-x11-2.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libgdk-x11-2.0.so.0.2400.32
/opt/Adobe/Reader9/Reader/intellinux/lib/libgraphite2.so.3
/opt/Adobe/Reader9/Reader/intellinux/lib/libgraphite2.so.3.2.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libgtk-x11-2.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libgtk-x11-2.0.so.0.2400.32
/opt/Adobe/Reader9/Reader/intellinux/lib/libharfbuzz.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libharfbuzz.so.0.20600.4
/opt/Adobe/Reader9/Reader/intellinux/lib/libidn.so.11
/opt/Adobe/Reader9/Reader/intellinux/lib/libidn.so.11.6.18
/opt/Adobe/Reader9/Reader/intellinux/lib/libpango-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpango-1.0.so.0.4400.7
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangocairo-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangocairo-1.0.so.0.4400.7
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoft2-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoft2-1.0.so.0.4400.7
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangox-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangox-1.0.so.0.0.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoxft-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoxft-1.0.so.0.4400.7
/opt/Adobe/Reader9/Reader/intellinux/lib/libpixman-1.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpixman-1.so.0.40.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libthai.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libthai.so.0.3.1

%changelog
* Fri Nov 27 2020 Jan Just Keijser <janjust@nikhef.nl> 2.0.0-1.fc32
- First version using Fedora 32 libraries

* Wed Dec 6 2017 Jan Just Keijser <janjust@nikhef.nl> 1.0.0-1.el7
- Initial version

