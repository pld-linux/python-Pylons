%define		fname		Pylons
Summary:	Pylons Web Framework
Summary(pl):	¦rodowisko WWW Pylons
Name:		python-%{fname}
Version:	0.9.3
Release:	0.2
License:	Pylons
Group:		Libraries/Python
Source0:	http://cheeseshop.python.org/packages/source/P/Pylons/%{fname}-%{version}.tar.gz
# Source0-md5:	1c36a3d58d81281a0f252a747ad38a00
URL:		http://pylonshq.com/
BuildRequires:	python-setuptools
BuildRequires:	python >= 1:2.5
%pyrequires_eq	python-modules
Requires:	python-Paste
Requires:	python-PasteDeploy
Requires:	python-simplejson >= 1.4
Requires:	python-FormEncode >= 0.6
Requires:	python-Myghty >= 1.1
Requires:	python-MyghtyUtils >= 0.52
Requires:	python-Beaker >= 0.6.1
Requires:	python-WebHelpers >= 0.2.2
Requires:	python-Routes >= 1.5.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pylons is a lightweight web framework emphasizing flexibility and
rapid development.

%description -l pl
Pylons to niedu¿e ¶rodowisko do szybkiego i elastycznego tworzenia
interaktywnych stron WWW.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/pylons
%{py_sitescriptdir}/%{fname}-%{version}-py*.egg-info
