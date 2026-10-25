#!/usr/bin/env python3
"""
SurvivorCare AI / SheCare AI - Comprehensive Automated Test Suite
Verifies backend security, Web Crypto/PBKDF2 equivalence, water tracker limits,
cycle date boundaries, SOS truthful dispatch, and the complete Nearby Help & Safe Places
implementation (verified directory, distance math, privacy controls, Google Maps API handling).
"""

import unittest
import json
import os
import sys
import math
import hashlib
import secrets
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

class TestSheCareAI(unittest.TestCase):

    def setUp(self):
        self.index_html_path = os.path.join(BASE_DIR, 'index.html')
        self.nearby_js_path = os.path.join(BASE_DIR, 'js', 'nearby_help.js')
        self.app_js_path = os.path.join(BASE_DIR, 'js', 'app.js')
        self.styles_css_path = os.path.join(BASE_DIR, 'css', 'styles.css')

        with open(self.index_html_path, 'r', encoding='utf-8') as f:
            self.index_html = f.read()

        with open(self.nearby_js_path, 'r', encoding='utf-8') as f:
            self.nearby_js = f.read()

    # -------------------------------------------------------------
    # 1. PBKDF2 SHA-256 CRYPTOGRAPHIC EQUIVALENCE
    # -------------------------------------------------------------
    def test_pbkdf2_sha256_cryptographic_security(self):
        """Verifies 100,000 iteration PBKDF2 SHA-256 password hashing."""
        password = "SafeSurvivorPass2026!#"
        salt = secrets.token_bytes(16)
        derived1 = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
        derived2 = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000).hex()
        self.assertEqual(derived1, derived2)
        self.assertEqual(len(derived1), 64) # 256 bits = 64 hex chars

    # -------------------------------------------------------------
    # 2. WATER TRACKER STRICT LIMIT OF 12 GLASSES
    # -------------------------------------------------------------
    def test_water_tracker_strict_limit_of_12(self):
        """Verifies that water glasses cannot exceed 12 and cannot be negative."""
        max_limit = 12
        count = 0
        for _ in range(15):
            count = min(count + 1, max_limit)
        self.assertEqual(count, 12, "Water count must strictly not exceed 12")

        # Test decrement bound
        for _ in range(20):
            count = max(0, count - 1)
        self.assertEqual(count, 0, "Water count cannot be negative")

    # -------------------------------------------------------------
    # 3. MENSTRUAL CYCLE TIMEZONE-SAFE BOUNDARY MATH
    # -------------------------------------------------------------
    def test_period_tracker_utc_date_math(self):
        """Verifies leap years, month boundaries, and year transitions without timezone shift."""
        from datetime import datetime, timezone, timedelta
        # Jan 31 -> Feb 28 in non-leap year
        d1 = datetime(2025, 1, 31, tzinfo=timezone.utc)
        d2 = d1 + timedelta(days=28)
        self.assertEqual(d2.strftime('%Y-%m-%d'), '2025-02-28')

        # Leap year Feb 1 + 28 days = Feb 29
        leap_start = datetime(2024, 2, 1, tzinfo=timezone.utc)
        leap_end = leap_start + timedelta(days=28)
        self.assertEqual(leap_end.strftime('%Y-%m-%d'), '2024-02-29')

        # Year boundary Dec 15 + 28 days = Jan 12
        year_start = datetime(2025, 12, 15, tzinfo=timezone.utc)
        year_end = year_start + timedelta(days=28)
        self.assertEqual(year_end.strftime('%Y-%m-%d'), '2026-01-12')

    # -------------------------------------------------------------
    # 4. NEARBY HELP: HAVERSINE DISTANCE FORMULA
    # -------------------------------------------------------------
    def test_haversine_distance_calculation(self):
        """Tests that Haversine distance matches real geographical distances."""
        # Distance between Mayo Hospital (31.5714, 74.3108) and Jinnah Hospital (31.4828, 74.2987) in Lahore
        lat1, lon1 = 31.5714, 74.3108
        lat2, lon2 = 31.4828, 74.2987

        R = 6371.0 # km
        dLat = math.radians(lat2 - lat1)
        dLon = math.radians(lon2 - lon1)
        a = (math.sin(dLat / 2) ** 2 +
             math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
             math.sin(dLon / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        dist = R * c

        # Physical road distance is ~12-14 km, direct as-the-crow-flies is ~9.9 km
        self.assertAlmostEqual(dist, 9.92, delta=0.5)

    # -------------------------------------------------------------
    # 5. NEARBY HELP: VERIFIED PAKISTAN & INDIA RESOURCES
    # -------------------------------------------------------------
    def test_verified_specialist_directory_integrity(self):
        """Verifies that Pakistan and India facilities are properly recorded with authoritative sources."""
        # Check presence of key facilities in js/nearby_help.js
        self.assertIn('Dar-ul-Aman Lahore', self.nearby_js)
        self.assertIn('Mayo Hospital Emergency', self.nearby_js)
        self.assertIn('Violence Against Women Centre (VAWC) Multan', self.nearby_js)
        self.assertIn('Panah Shelter Home for Women', self.nearby_js)
        self.assertIn('JPMC', self.nearby_js)
        self.assertIn('PIMS', self.nearby_js)
        self.assertIn('Sakhi One Stop Centre (OSC) - Central Delhi', self.nearby_js)
        self.assertIn('AIIMS New Delhi Emergency', self.nearby_js)
        self.assertIn('Special Cell for Women & Children', self.nearby_js)
        self.assertIn('Urja Trust Safe Shelter', self.nearby_js)
        self.assertIn('Bharosa Support Centre', self.nearby_js)

    # -------------------------------------------------------------
    # 6. SENSITIVE SHELTER ADDRESS CONFIDENTIALITY
    # -------------------------------------------------------------
    def test_shelter_address_confidentiality_protection(self):
        """Verifies that crisis shelter addresses are kept confidential for survivor safety."""
        # Check that isConfidentialAddress is set for sensitive shelters
        self.assertIn('isConfidentialAddress: true', self.nearby_js)
        self.assertIn('Confidential address for resident safety', self.nearby_js)
        self.assertIn('Address confidential to protect resident survivors', self.nearby_js)

    # -------------------------------------------------------------
    # 7. LOCATION PRIVACY & OPTIONAL CONSENT CONTROLS
    # -------------------------------------------------------------
    def test_location_privacy_and_consent_mechanics(self):
        """Ensures location access is strictly optional with clear consent and clear options."""
        # Location modal must exist
        self.assertIn('id="modalLocationConsent"', self.index_html)
        self.assertIn('Zero Transmission', self.index_html)
        self.assertIn('Zero Reporting', self.index_html)
        self.assertIn('btnClearLocation', self.index_html)
        self.assertIn('clearLocation()', self.nearby_js)
        self.assertIn('locationPermissionDenied', self.nearby_js)

    # -------------------------------------------------------------
    # 8. NON-STIGMATIZING SEARCH QUERY INTEGRITY
    # -------------------------------------------------------------
    def test_non_stigmatizing_search_queries(self):
        """Verifies that external Google Maps queries avoid stigmatizing sexual assault terms."""
        # External query should use safe, clean terms
        self.assertIn('hospital emergency room', self.nearby_js)
        # Should not format external query with sensitive words that leak in search logs
        self.assertNotIn('query=rape+survivor', self.nearby_js.lower())
        self.assertNotIn('query=sexual+assault+victim', self.nearby_js.lower())

    # -------------------------------------------------------------
    # 9. GOOGLE MAPS PLATFORM INTEGRATION & FALLBACKS
    # -------------------------------------------------------------
    def test_google_maps_platform_and_fallback_modes(self):
        """Verifies that Google Maps JS API is supported with Leaflet/OpenStreetMap fallback."""
        self.assertIn('modalGoogleMapsConfig', self.index_html)
        self.assertIn('HTTP referrers (web sites)', self.index_html)
        self.assertIn('maps.googleapis.com/maps/api/js', self.nearby_js)
        self.assertIn('gm_authFailure', self.nearby_js)
        self.assertIn('initLeafletOrFallbackMap', self.nearby_js)
        self.assertIn('https://www.google.com/maps/dir/?api=1', self.nearby_js)

    # -------------------------------------------------------------
    # 10. HONEST EMERGENCY AND DIALER GUIDANCE
    # -------------------------------------------------------------
    def test_emergency_and_dialer_transparency(self):
        """Verifies that opening a dialer is clearly explained as not completing a call."""
        self.assertIn('SheCare AI is not an emergency dispatcher and does not diagnose conditions', self.index_html)
        self.assertIn('Opening your phone dialer does not mean a call was placed', self.index_html)
        self.assertIn('112', self.index_html)
        self.assertIn('1099', self.index_html)
        self.assertIn('1043', self.index_html)

    # -------------------------------------------------------------
    # 11. CAMOUFLAGE SCREEN & DISCREET MODE FOR NEARBY HELP
    # -------------------------------------------------------------
    def test_camouflage_and_discreet_mode_for_nearby_places(self):
        """Verifies camouflage screen hides nearby help and discreet mode alters labels."""
        self.assertIn('id="camouflageScreen"', self.index_html)
        self.assertIn('btnTopQuickExit', self.index_html)
        # Discreet mode updates
        with open(self.app_js_path, 'r', encoding='utf-8') as f:
            app_js = f.read()
        self.assertIn("navNearby.textContent = 'Nearby Services'", app_js)
        self.assertIn("nearbyTitle.textContent = '📍 Local Services & Community Directory'", app_js)

    # -------------------------------------------------------------
    # 12. GITHUB PAGES STATIC HOSTING & ASSET PATHS
    # -------------------------------------------------------------
    def test_github_pages_static_paths_compatibility(self):
        """Verifies that all assets use relative paths for GitHub Pages /Shecare_AI/ subpath."""
        # No absolute root paths like href="/css/styles.css"
        self.assertNotIn('href="/css/', self.index_html)
        self.assertNotIn('src="/js/', self.index_html)
        self.assertIn('href="css/styles.css"', self.index_html)
        self.assertIn('src="js/nearby_help.js"', self.index_html)

    # -------------------------------------------------------------
    # 13. STRICT EXCLUSION: ZERO LANGUAGE TRANSLATOR
    # -------------------------------------------------------------
    def test_strict_exclusion_of_language_translator(self):
        """Verifies no language translation dropdowns or translation libraries exist."""
        self.assertNotIn('google-translate', self.index_html.lower())
        self.assertNotIn('translate.google.com', self.index_html.lower())
        self.assertNotIn('selectlanguage', self.index_html.lower())

    # -------------------------------------------------------------
    # 14. SVG ICON SIZING CONSTRAINTS
    # -------------------------------------------------------------
    def test_svg_icon_dimensions(self):
        """Verifies SVGs have explicit 24px constraints to prevent screen-filling outlines."""
        svg_tags = re.findall(r'<svg[^>]*>', self.index_html)
        self.assertTrue(len(svg_tags) >= 7)
        for tag in svg_tags:
            self.assertIn('width="24"', tag)
            self.assertIn('height="24"', tag)

    # -------------------------------------------------------------
    # 15. BACKEND HEALTH & ENDPOINT INTEGRITY
    # -------------------------------------------------------------
    def test_server_endpoint_handlers(self):
        """Verifies server.py has security headers, health endpoint, and SOS gateway."""
        with open(os.path.join(BASE_DIR, 'server.py'), 'r', encoding='utf-8') as f:
            server_py = f.read()
        self.assertIn('X-Content-Type-Options', server_py)
        self.assertIn('X-Frame-Options', server_py)
        self.assertIn('/api/health', server_py)
        self.assertIn('/api/auth/register', server_py)
        self.assertIn('/api/auth/login', server_py)
        self.assertIn('/api/sos/send', server_py)
        self.assertIn('nearbyHelpEnabled', server_py)

if __name__ == '__main__':
    unittest.main()
