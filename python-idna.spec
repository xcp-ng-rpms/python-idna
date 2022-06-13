%global srcname idna

Name:           python-%{srcname}
Version:        3.3
Release:        3%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD and Python and Unicode
URL:            https://github.com/kjd/idna
Source0:        https://pypi.io/packages/source/i/%{srcname}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%package -n python3-%{srcname}
Summary:        Internationalized Domain Names in Applications (IDNA)
%{?python_provide:%python_provide python%{python3_pkgversion}-%{srcname}}

%description -n python3-%{srcname}
A library to support the Internationalised Domain Names in Applications (IDNA)
protocol as specified in RFC 5891 <http://tools.ietf.org/html/rfc5891>.  This
version of the protocol is often referred to as "IDNA2008" and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement for the
"encodings.idna" module that comes with the Python standard library but
currently only supports the older 2003 specification.

%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove bundled egg-info
rm -rf %{srcname}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test


%files -n python3-%{srcname}
%license LICENSE.md
%doc README.rst HISTORY.rst
%{python3_sitelib}/%{srcname}
%{python3_sitelib}/%{srcname}-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Oct 14 2021 Lumír Balhar <lbalhar@redhat.com> - 3.3-1
- Update to 3.3
Resolves: rhbz#2013470

* Tue Aug 03 2021 Lumír Balhar <lbalhar@redhat.com> - 3.2-1
- Update to 3.2
Resolves: rhbz#1965774

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 2.10-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Lumír Balhar <lbalhar@redhat.com> - 2.10-1
- Update to 2.10 (#1851653)

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 2.9-2
- Rebuilt for Python 3.9

* Tue May 05 2020 Lumír Balhar <lbalhar@redhat.com> - 2.9-1
- Update to 2.9 (#1803654)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8-5
- Subpackage python2-idna has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.8-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 28 2019 Jeremy Cline <jcline@redhat.com> - 2.8-1
- Update to v2.8
- Drop python version conditionals

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.7-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Jeremy Cline <jeremy@jcline.org> - 2.7-1
- Update to v2.7 (rhbz 1589803)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 19 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.5-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Mar 07 2017 Jeremy Cline <jeremy@jcline.org> - 2.5-1
- Update to version 2.5

* Wed Mar 01 2017 Jeremy Cline <jeremy@jcline.org> - 2.4-1
- Update to version 2.4

* Tue Feb 28 2017 Paul Wouters <pwouters@redhat.com> - 2.3-1
- Resolves: rhbz#1427499 Update to 2.3 for IDNAError bugfix and memory improvement

* Thu Feb 09 2017 Jeremy Cline <jeremy@jcline.org> - 2.2-1
- Update to version 2.2 (#1406757)

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.1-3
- Rebuild for Python 3.6

* Mon Nov 28 2016 Orion Poplawski <orion@cora.nwra.com> - 2.1-2
- Ship python2-idna
- Enable python3 for EPEL
- Modernize spec

* Mon Oct 17 2016 tom.prince@ualberta.net - 2.1-1
- Bump version.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 04 2015 Robert Kuska <rkuska@redhat.com> - 2.0-2
- Rebuilt for Python3.5 rebuild

* Thu Aug 13 2015 Paul Wouters <pwouters@redhat.com> - 2.0-1
- Update to 2.0 which is required by python-cryptography

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Dec 31 2014 tom.prince@ualberta.net - 1.0-1
- Bump version.

* Mon Oct 27 2014 tom.prince@ualberta.net - 0.8-3
- Update licences.

* Sat Jul 12 2014 tom.prince@ualberta.net - 0.8-2
- Be more specfic about .egg-info directories.
- Use python2-devel

* Sat Jul 12 2014 tom.prince@ualberta.net - 0.8-1
- Initial package.
