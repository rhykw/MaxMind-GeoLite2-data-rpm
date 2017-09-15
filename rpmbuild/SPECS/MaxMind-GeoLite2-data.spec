Name:		MaxMind-GeoLite2-data
# The geolite databases are updated on the first Tuesday of each month,
# hence we use a versioning scheme of YYYY.MM for the Fedora package
Version:	2017.09
Release:	1%{?dist}
Summary:	Free GeoLite2 IP geolocation country database
# License specified at http://dev.maxmind.com/geoip/legacy/geolite/#License
License:	CC-BY-SA
URL:		https://dev.maxmind.com/geoip/geoip2/geolite2/
Source0:	http://geolite.maxmind.com/download/geoip/database/GeoLite2-Country.tar.gz
Source1:	http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.tar.gz
Source2:	http://geolite.maxmind.com/download/geoip/database/GeoLite2-ASN.tar.gz
BuildArch:	noarch

# This data has previously been available in differently-named packages
Provides:	GeoIP2-data = %{version}
Provides:	geoip2-geolite2 = %{version}

%description
The GeoLite2 databases are free IP geolocation databases. This package contains
a database that maps IP addresses to countries.

This product includes GeoLite2 data created by MaxMind, available from
http://www.maxmind.com/

%package extra
Summary:	Free GeoLite2 IP geolocation databases
License:	CC-BY-SA
Requires:	%{name} = %{version}-%{release}

%description extra
The GeoLite2 databases are free IP geolocation databases. This package contains
databases that map IP addresses to cities and autonomous system numbers.

This product includes GeoLite data created by MaxMind, available from
http://www.maxmind.com/

%prep
%setup -q -T -c

tar -zx --strip=1 -f %{SOURCE0} GeoLite2-\*.mmdb
tar -zx --strip=1 -f %{SOURCE1} GeoLite2-\*.mmdb
tar -zx --strip=1 -f %{SOURCE2} GeoLite2-\*.mmdb

%build
# This section intentionally left empty

%install
mkdir -p %{buildroot}%{_datadir}/GeoIP2/
for db in \
	GeoLite2-*.mmdb
do
	install -p -m 644 $db %{buildroot}%{_datadir}/GeoIP2/
done

%files
%dir %{_datadir}/GeoIP2/
# The databases are %%verify(not md5 size mtime) so that they can be updated
# via cron scripts and rpm will not moan about the files having changed
%verify(not md5 size mtime) %{_datadir}/GeoIP2/GeoLite2-Country.mmdb

%files extra
# The databases are %%verify(not md5 size mtime) so that they can be updated
# via cron scripts and rpm will not moan about the files having changed
%verify(not md5 size mtime) %{_datadir}/GeoIP2/GeoLite2-City.mmdb
%verify(not md5 size mtime) %{_datadir}/GeoIP2/GeoLite2-ASN.mmdb

%changelog
* Sun Jul 23 2017 Paul Howarth <paul@city-fan.org> - 2017.07-1
- Update to July 2017 databases
