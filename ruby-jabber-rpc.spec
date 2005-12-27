Summary:	Jabber-RPC library for Ruby
Summary(pl):	Biblioteka Jabber-RPC dla jêzyka Ruby
Name:		ruby-jabber-rpc
Version:	0.0.20041208
Release:	3
License:	GPL
Group:		Development/Languages
# from http://jabber-rpc.rubyforge.org via darcs
Source0:	jabber-rpc-20041208.tar.gz
# Source0-md5:	a5151ae6806def5c5ddeb4a7500e2fc6
Source1:	setup.rb
URL:		http://jabber-rpc.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby-modules
BuildRequires:	ruby-devel
Requires:	ruby-modules
Requires:	ruby-jabber4r
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jabber-RPC library for Ruby.

%description -l pl
Biblioteka Jabber-RPC dla jêzyka Ruby.

%prep
%setup -q -n jabber-rpc.rubyforge.org
mkdir -p lib/jabber
mv rpc.rb lib/jabber/rpc.rb
install %{SOURCE1} setup.rb

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/jabber/rpc.rb
# Does not merge well with others.
%{ruby_ridir}/Jabber/RPC
