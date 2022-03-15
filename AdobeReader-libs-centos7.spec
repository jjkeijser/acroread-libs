
%define debug_package %{nil}
#%define __arch_install_post %{nil}
#%define __os_install_post %{nil}
#%define __spec_install_post %{nil}

BuildArch:     i686
Name:          AdobeReader-libs
Version:       1.0.0
Release:       1%{?dist}
License:       Commercial 
Group:         Applications/Publishing
Summary:       Adobe Reader compatibility libraries for CentOS 7
URL:           https://github.com/jjkeijser/acroread-libs

Source:        AdobeReader-libs-%{version}.tar.gz
AutoProv:      no
AutoReq:       no

Provides:      libGL.so.1
Provides:      libGLU.so.1
Provides:      libcairo.so.2
Provides:      libgdk-x11-2.0.so.0
Provides:      libgtk-x11-2.0.so.0
Provides:      libpango-1.0.so.0
Provides:      libpangocairo-1.0.so.0
Provides:      libpangoft2-1.0.so.0
Provides:      libpangox-1.0.so.0
Provides:      libpangoxft-1.0.so.0

%description
Compatibility libraries to allow you to run AdobeReader on CentOS 7.

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
/opt/Adobe/Reader9/Reader/intellinux/lib/libGL.so.1.2.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLU.so.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libGLU.so.1.3.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libcairo.so.2
/opt/Adobe/Reader9/Reader/intellinux/lib/libcairo.so.2.10800.8
/opt/Adobe/Reader9/Reader/intellinux/lib/libgdk-x11-2.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libgdk-x11-2.0.so.0.2400.23
/opt/Adobe/Reader9/Reader/intellinux/lib/libgtk-x11-2.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libgtk-x11-2.0.so.0.2400.23
/opt/Adobe/Reader9/Reader/intellinux/lib/libpango-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpango-1.0.so.0.2800.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangocairo-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangocairo-1.0.so.0.2800.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoft2-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoft2-1.0.so.0.2800.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangox-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangox-1.0.so.0.2800.1
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoxft-1.0.so.0
/opt/Adobe/Reader9/Reader/intellinux/lib/libpangoxft-1.0.so.0.2800.1

%changelog
* Wed Dec 6 2017 Jan Just Keijser <janjust@nikhef.nl> 1.0.0-1.el7
- Initial version

