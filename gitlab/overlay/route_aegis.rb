# frozen_string_literal: true

get '/-/aegis/projects/:project_id',
  to: 'aegis/supervision#show',
  as: :aegis_project_supervision
