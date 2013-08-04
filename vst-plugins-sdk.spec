Summary:	VST audio plugins SDK
Name:		vst-plugins-sdk
Version:	2.4
Release:	4
License:	Other
Group:		Development
Source0:	vst_sdk2_4_rev2.zip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
VST 2.4 Audio Plug-Ins SDK.

%prep
%setup -qc

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/vst

install vstsdk2.4/pluginterfaces/vst2.x/*.h $RPM_BUILD_ROOT%{_includedir}/vst

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_includedir}/vst

