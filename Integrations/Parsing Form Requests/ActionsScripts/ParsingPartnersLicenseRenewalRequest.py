from SiemplifyAction import *
import re
import datetime


def main():
    siemplify = SiemplifyAction()

    enriched_entities = []
    for alert in siemplify.case.alerts:
        for event in alert.security_events:
            name = event.additional_properties['body'].encode('utf-8')
            FirstName = re.findall(r'First Name [^A-Za-z]+([A-Za-z]+)', name)[0]
            LastName = re.findall(r'Last Name [^A-Za-z]+([A-Za-z]+)', name)[0]
            Company = re.findall(r'Company [^A-Za-z]+([A-Za-z]+)', name)[0]

            Country = "Israel"

            FirstName = unicode(FirstName, errors='ignore').strip()
            LastName = unicode(LastName, errors='ignore').strip()
            enrichment_json = {}
            enrichment_json['FirstName'] = FirstName
            enrichment_json['LastName'] = LastName
            enrichment_json['Country'] = Country
            enrichment_json['Company'] = Company
            print(enrichment_json)
            now = datetime.datetime.now()

            # Adding First and Last name to target entities
            for entity in siemplify.target_entities:
                entity.additional_properties['FirstName'] = FirstName
                entity.additional_properties['LastName'] = LastName
                entity.additional_properties['Country'] = Country
                entity.additional_properties['Company'] = Company
                entity.additional_properties['CreationTime'] = '{0}/{1}/{2}'.format(now.day,now.month,now.year)
                entity.additional_properties['CreationTime_Year'] = now.year
                entity.additional_properties['CreationTime_Month'] = now.month
                entity.additional_properties['CreationTime_Day'] = now.day
                entity.additional_properties['CreationTime_Week'] = now.strftime("%V")

                enriched_entities.append(entity)
    if len(enriched_entities) > 0:
        siemplify.update_entities(enriched_entities)
   
    siemplify.result.add_json('Email Enrichment Data', enrichment_json)
    siemplify.result.add_result_json(enrichment_json)
    output_message = str(len(enriched_entities)) + ' entities were enriched.'
    result_value = 'true'
    siemplify.end(output_message, result_value)


if __name__ == "__main__":
    main()