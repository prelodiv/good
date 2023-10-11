class XMLGraphExporter:
    def export_graph_to_xml(self, graph):
        xml_data = "<Graph>"

        for node in graph.get_nodes():
            xml_data += node.to_xml()

        xml_data += "</Graph>"
        return xml_data
