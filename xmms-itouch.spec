%define libdir	%(eval "%{_bindir}/xmms-config --general-plugin-dir")
%define datadir	%(eval "%{_bindir}/xmms-config --data-dir")

Name:		xmms-itouch
Version:	0.1.2
Release:	%mkrel 4
Epoch:		0
Summary:	XMMS iTouch keyboard control plugin
License:	GPL
Group:		Sound
URL:		http://www.saunalahti.fi/~syrjala/xmms-itouch/
Source0:	http://www.saunalahti.fi/~syrjala/xmms-itouch/%{name}-%{version}.tar.bz2
Source1:	http://www.saunalahti.fi/~syrjala/xmms-itouch/%{name}.config
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	xmms >= 0:1.2.0
BuildRequires:	xmms-devel >= 0:1.2.0

%description
With this XMMS plugin you can take advantage of the multimedia (playback and
volume control) keys on your Logitech iTouch keyboard. When the plugin is
used you can use the keys regardless of the current input focus. The plugin
won't work if some other application (eg. xscreensaver) has grabbed the
keyboard.
	
%prep
%setup -q
%{__install} -m 644 %{SOURCE1} %{name}.config

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%{libdir}/*
%{datadir}/xmms-itouch.config

