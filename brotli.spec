%define _prefix      /usr/local
%define _share_dir   %{_prefix}/share/

Summary: Lossless compression algorithm
Name: brotli
Version: %{version}
Release: %{release}
License: MIT
URL: https://github.com/google/brotli
Source: brotli-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Prefix: %{_prefix}
Vendor: Google
Packager: Denis Valchuk
Provides: brotli

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%prep
%setup -n brotli

%install
mkdir -p $RPM_BUILD_ROOT%{_prefix}/bin
mkdir -p $RPM_BUILD_ROOT%{_share_dir}/licenses/brotli-%{version}/
mkdir -p $RPM_BUILD_ROOT%{_libdir}
install -p -D -m 755 brotli $RPM_BUILD_ROOT%{_prefix}/bin/brotli
install -p -D -m 755 LICENSE $RPM_BUILD_ROOT%{_share_dir}/licenses/brotli-%{version}/
install -p -D -m 755 libbrotlicommon.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install -p -D -m 755 libbrotlidec.so.%{version} $RPM_BUILD_ROOT%{_libdir}
install -p -D -m 755 libbrotlienc.so.%{version} $RPM_BUILD_ROOT%{_libdir}
ln -s $RPM_BUILD_ROOT%{_libdir}/libbrotlicommon.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libbrotlicommon.so.1
ln -s $RPM_BUILD_ROOT%{_libdir}/libbrotlidec.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libbrotlidec.so.1
ln -s $RPM_BUILD_ROOT%{_libdir}/libbrotlienc.so.%{version} $RPM_BUILD_ROOT%{_libdir}/libbrotlienc.so.1


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_share_dir}/*
%{_libdir}/*
%attr(0755,root,root) %{_prefix}/bin
