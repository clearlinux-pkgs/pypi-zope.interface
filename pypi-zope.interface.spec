#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-zope.interface
Version  : 5.4.0
Release  : 82
URL      : https://files.pythonhosted.org/packages/ae/58/e0877f58daa69126a5fb325d6df92b20b77431cd281e189c5ec42b722f58/zope.interface-5.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ae/58/e0877f58daa69126a5fb325d6df92b20b77431cd281e189c5ec42b722f58/zope.interface-5.4.0.tar.gz
Summary  : Interfaces for Python
Group    : Development/Tools
License  : ZPL-2.1
Requires: pypi-zope.interface-filemap = %{version}-%{release}
Requires: pypi-zope.interface-lib = %{version}-%{release}
Requires: pypi-zope.interface-license = %{version}-%{release}
Requires: pypi-zope.interface-python = %{version}-%{release}
Requires: pypi-zope.interface-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)

%description
``zope.interface``
        ====================

%package filemap
Summary: filemap components for the pypi-zope.interface package.
Group: Default

%description filemap
filemap components for the pypi-zope.interface package.


%package lib
Summary: lib components for the pypi-zope.interface package.
Group: Libraries
Requires: pypi-zope.interface-license = %{version}-%{release}
Requires: pypi-zope.interface-filemap = %{version}-%{release}

%description lib
lib components for the pypi-zope.interface package.


%package license
Summary: license components for the pypi-zope.interface package.
Group: Default

%description license
license components for the pypi-zope.interface package.


%package python
Summary: python components for the pypi-zope.interface package.
Group: Default
Requires: pypi-zope.interface-python3 = %{version}-%{release}

%description python
python components for the pypi-zope.interface package.


%package python3
Summary: python3 components for the pypi-zope.interface package.
Group: Default
Requires: pypi-zope.interface-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(zope.interface)
Requires: pypi(setuptools)

%description python3
python3 components for the pypi-zope.interface package.


%prep
%setup -q -n zope.interface-5.4.0
cd %{_builddir}/zope.interface-5.4.0
pushd ..
cp -a zope.interface-5.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653003453
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-zope.interface
cp %{_builddir}/zope.interface-5.4.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-zope.interface/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-zope.interface

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-zope.interface/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
