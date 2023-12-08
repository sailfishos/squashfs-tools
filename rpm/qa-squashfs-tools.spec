
Name:		squashfs-tools
Summary:	Utility for the creation of squashfs filesystems
Version:	4.6.1
Release:	1
License:	GPLv2+
URL:		http://squashfs.sourceforge.net
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	zlib-devel
BuildRequires:	xz-devel
BuildRequires:	lzo-devel
BuildRequires:	libattr-devel

%description
Squashfs is a highly compressed read-only filesystem for Linux. This package
contains the utilities for manipulating squashfs filesystems.

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
XZ_SUPPORT=1 LZO_SUPPORT=1 LZMA_XZ_SUPPORT=1 make -C squashfs-tools %{?jobs:-j%jobs}

%install
install -D -m 755 squashfs-tools/mksquashfs %{buildroot}%{_sbindir}/mksquashfs
install -D -m 755 squashfs-tools/unsquashfs %{buildroot}%{_sbindir}/unsquashfs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license COPYING
%doc README

%{_sbindir}/mksquashfs
%{_sbindir}/unsquashfs
