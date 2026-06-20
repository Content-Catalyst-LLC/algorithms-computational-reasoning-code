% Educational Prolog rules for secure-communication governance.

strong_case(web_service_secure_channel).
weak_case(legacy_encrypted_file_transfer).

requires_review(Case) :- weak_case(Case).
requires_key_rotation(Case) :- strong_case(Case); weak_case(Case).
requires_certificate_validation(web_service_secure_channel).
requires_incident_response(Case) :- strong_case(Case); weak_case(Case).
